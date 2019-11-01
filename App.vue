<template>
  <view class="container">
    <view v-if="isNotStarted">
      <text class="copywrite">{{copywrite}}</text>
      <view class="gold-button-back">
        <button class="gold-button" :on-press="go" title="운명 개척하러 가기" color="white"></button>
      </view>
    </view>
    <view class="container" v-if="isStarted">
      <touchable-opacity :on-press="onIconClicked">
        <image :style="{width: 100, height: 100}" :source="image" />
      </touchable-opacity>
      <text class="title" v-if="luck_selected">오늘의 운세는 {{lucktype}}입니다.</text>
      <text class="title" v-if="luck_unselected">운세를 직접 골라보세요!</text>
      <text class="description">{{text}}</text>
      <text class="lucky-item" v-if="luck_selected">행운의 아이템</text>
      <view class="lucky-items" v-if="luck_selected">
        <touchable-opacity :on-press="onItemClicked1">
          <image class="item" :style="{width: 60, height: 60}" :source="item1" />
        </touchable-opacity>
        <touchable-opacity :on-press="onItemClicked2">
          <image class="item" :style="{width: 60, height: 60}" :source="item2" />
        </touchable-opacity>
        <touchable-opacity :on-press="onItemClicked3">
          <image class="item" :style="{width: 60, height: 60}" :source="item3" />
        </touchable-opacity>
      </view>
    </view>
  </view>
</template>

<style>
.container {
  background-color: white;
  align-items: center;
  justify-content: center;
  flex: 1;
}
.title {
  font-size: 24;
  font-weight: bold;

  margin-top: 20;
}

.description {
  margin-top: 10;
  padding-left: 40;
  padding-right: 40;
}

.layer {
  background-color: #000000;
  opacity: 0.1;

  width: 100;
  height: 100;

  align-items: center;
  justify-content: center;
}

.lucky-item {
  margin-top: 50;
  font-size: 22;
  font-weight: bold;
}

.lucky-items {
  flex-direction: row;

  margin-top: 15;
}

.item {
  margin-left: 10;
  margin-right: 10;
}

.copywrite {
  text-align: left;
  font-size: 40;
  line-height: 55;

  padding-right: 70;
  padding-bottom: 400;
}

.gold-button-back {
  background-color: #42b883;
  padding: 10;
  border-radius: 10;
}
</style>

<script>
import luck from "./assets/luck.json";
import money_image from "./assets/money.png";
import health_image from "./assets/health.png";
import love_image from "./assets/love.png";
import business_image from "./assets/business.png";
import plus_image from "./assets/plus.png";

import item_book from "./assets/items/book.png";
import item_coffee from "./assets/items/coffee.png";
import item_phone from "./assets/items/phone.png";
import item_chair from "./assets/items/chair.png";
import item_glasses from "./assets/items/glasses.png";
import item_pants from "./assets/items/pants.png";
import item_pencil from "./assets/items/pencil.png";
import item_shoes from "./assets/items/shoes.png";
import item_watch from "./assets/items/watch.png";

import { Alert } from "react-native";

export default {
  data: {
    luck: luck,
    lucktype: "???",
    text_index: 0,
    items: [
      plus_image,
      item_book,
      item_coffee,
      item_phone,
      item_chair,
      item_glasses,
      item_pants,
      item_pencil,
      item_shoes,
      item_watch
    ],
    item_index: [0, 0, 0],
    accelerometerData: {},
    copywrite: "아들아, 언제까지\n정해준 대로만\n살 거니?",
    start: false
  },
  computed: {
    isStarted: function() {
      return this.start;
    },
    isNotStarted: function() {
      return !this.isStarted;
    },
    text: function() {
      return luck.filter(l => l.name === this.lucktype)[0].text[this.text_index]
        .msg;
    },
    keyword: function() {
      return luck.filter(l => l.name === this.lucktype)[0].text[this.text_index]
        .key;
    },
    image: function() {
      let f = luck.filter(l => l.name === this.lucktype)[0];

      let img = plus_image;
      if (this.lucktype === "재물운") {
        img = money_image;
      } else if (this.lucktype === "사업운") {
        img = business_image;
      } else if (this.lucktype === "애정운") {
        img = love_image;
      } else if (this.lucktype === "건강운") {
        img = health_image;
      }
      return img;
    },
    luck_selected: function() {
      return this.lucktype !== "???";
    },
    luck_unselected: function() {
      return this.lucktype === "???";
    },
    item1: function() {
      return this.items[this.item_index[0]];
    },
    item2: function() {
      return this.items[this.item_index[1]];
    },
    item3: function() {
      return this.items[this.item_index[2]];
    }
  },
  methods: {
    go: function() {
      this.start = true;
    },
    onIconClicked: function() {
      Alert.alert(
        "운세 선택",
        "오늘의 운세는 어떤가요?",
        [
          {
            text: "재물운",
            onPress: () => {
              let texts = [];
              let text = luck.filter(l => l.name === "재물운")[0].text;
              while (texts.length < 3) {
                let index = Math.floor(Math.random() * text.length);
                var rand = text[index].key;
                if (texts.includes(text[index].msg)) {
                  continue;
                }
                texts.push({
                  text: rand,
                  onPress: () => {
                    this.lucktype = "재물운";
                    this.text_index = index;
                  }
                });
              }

              Alert.alert("상세 선택", "어떤 운세를 바라시나요?", texts, {
                cancelable: true
              });
            }
          },
          {
            text: "사업운",
            onPress: () => {
              let texts = [];
              let text = luck.filter(l => l.name === "사업운")[0].text;
              while (texts.length < 3) {
                let index = Math.floor(Math.random() * text.length);
                var rand = text[index].key;
                if (texts.includes(text[index].msg)) {
                  continue;
                }
                texts.push({
                  text: rand,
                  onPress: () => {
                    this.lucktype = "사업운";
                    this.text_index = index;
                  }
                });
              }

              Alert.alert("상세 선택", "어떤 운세를 바라시나요?", texts, {
                cancelable: true
              });
            }
          },
          {
            text: "애정운",
            onPress: () => {
              let texts = [];
              let text = luck.filter(l => l.name === "애정운")[0].text;
              while (texts.length < 3) {
                let index = Math.floor(Math.random() * text.length);
                var rand = text[index].key;
                if (texts.includes(text[index].msg)) {
                  continue;
                }
                texts.push({
                  text: rand,
                  onPress: () => {
                    this.lucktype = "애정운";
                    this.text_index = index;
                  }
                });
              }

              Alert.alert("상세 선택", "어떤 운세를 바라시나요?", texts, {
                cancelable: true
              });
            }
          },
          {
            text: "건강운",
            onPress: () => {
              let texts = [];
              let text = luck.filter(l => l.name === "건강운")[0].text;
              while (texts.length < 3) {
                let index = Math.floor(Math.random() * text.length);
                var rand = text[index].key;
                if (texts.includes(text[index].msg)) {
                  continue;
                }
                texts.push({
                  text: rand,
                  onPress: () => {
                    this.lucktype = "건강운";
                    this.text_index = index;
                  }
                });
              }

              Alert.alert("상세 선택", "어떤 운세를 바라시나요?", texts, {
                cancelable: true
              });
            }
          }
        ],
        { cancelable: true }
      );
    },
    onItemClicked1: function() {
      let items = [];
      while (items.length < 3) {
        let index = Math.floor(Math.random() * this.items.length);
        if (items.includes(index) || index === 0) {
          continue;
        }
        items.push(index);
      }
      this.item_index = items;
    },
    onItemClicked2: function() {
      let items = [];
      while (items.length < 3) {
        let index = Math.floor(Math.random() * this.items.length);
        if (items.includes(index) || index === 0) {
          continue;
        }
        items.push(index);
      }
      this.item_index = items;
    },
    onItemClicked3: function() {
      let items = [];
      while (items.length < 3) {
        let index = Math.floor(Math.random() * this.items.length);
        if (items.includes(index) || index === 0) {
          continue;
        }
        items.push(index);
      }
      this.item_index = items;
    }
  }
};
</script>