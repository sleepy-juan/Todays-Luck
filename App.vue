<template>
  <view class="container">
    <touchable-opacity :on-press="onIconClicked">
      <image :style="{width: 100, height: 100}" :source="image" />
    </touchable-opacity>
    <text class="title">오늘의 운세는 {{lucktype}}입니다.</text>
    <text class="description">{{text}}</text>
    <text class="lucky-item" v-if="luck_selected">행운의 아이템</text>
    <view class="lucky-items" v-if="luck_selected">
      <image class="item" :style="{width: 60, height: 60}" :source="item1" />
      <image class="item" :style="{width: 60, height: 60}" :source="item2" />
      <image class="item" :style="{width: 60, height: 60}" :source="item3" />
    </view>

    <status-bar background-color="blue" bar-style="light-content" />
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

import { Alert } from "react-native";

export default {
  data: {
    luck: luck,
    lucktype: "???",
    text_index: 0,
    items: [item_book, item_coffee, item_phone]
  },
  computed: {
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
    item1: function() {
      return this.items[0];
    },
    item2: function() {
      return this.items[1];
    },
    item3: function() {
      return this.items[2];
    }
  },
  methods: {
    onIconClicked: function() {
      Alert.alert("운세 선택", "오늘의 운세는 어떤가요?", [
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

            Alert.alert("상세 선택", "어떤 운세를 바라시나요?", texts);
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

            Alert.alert("상세 선택", "어떤 운세를 바라시나요?", texts);
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

            Alert.alert("상세 선택", "어떤 운세를 바라시나요?", texts);
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

            Alert.alert("상세 선택", "어떤 운세를 바라시나요?", texts);
          }
        }
      ]);
    }
  }
};
</script>