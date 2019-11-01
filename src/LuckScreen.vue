<template>
  <view class="container">
    <touchable-opacity :on-press="onIconClicked">
      <image :style="{width: 100, height: 100}" :source="image" />
    </touchable-opacity>
    <text class="title">오늘의 운세는 {{lucktype}}입니다.</text>
    <text class="description">{{text}}</text>

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
  margin-top: 20;
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
</style>


<script>
import luck from "../assets/luck.json";
import money_image from "../assets/money.png";
import health_image from "../assets/health.png";
import love_image from "../assets/love.png";
import business_image from "../assets/business.png";
import plus_image from "../assets/plus.png";

import { Alert } from "react-native";

export default {
  data: {
    luck: luck,
    lucktype: "???",
    text_index: 0
  },
  computed: {
    text: function() {
      return luck.filter(l => l.name === this.lucktype)[0].text[
        this.text_index
      ];
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
              var rand = text[index];
              if (texts.includes(rand)) {
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
              var rand = text[index];
              if (texts.includes(rand)) {
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
              var rand = text[index];
              if (texts.includes(rand)) {
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
              var rand = text[index];
              if (texts.includes(rand)) {
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