<template>
  <view class="container">
    <touchable-opacity :on-press="onIconClicked">
      <image :style="{width: 100, height: 100}" :source="image" />
    </touchable-opacity>
    <text class="title">오늘의 운세는 {{lucktype}}입니다.</text>
    <text class="description">{{text}}</text>
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
</style>

<script>
import luck from "./assets/luck.json";
import money_image from "./assets/money.png";
import health_image from "./assets/health.png";
import love_image from "./assets/love.png";
import business_image from "./assets/business.png";

import { Alert } from "react-native";

let lucktype = "사업운";

export default {
  data: function() {
    let f = luck.filter(l => l.name === lucktype)[0];

    let img = money_image;
    if (lucktype === "사업운") {
      img = business_image;
    } else if (lucktype === "연애운") {
      img = love_image;
    } else if (lucktype === "건강운") {
      img = health_image;
    }

    return {
      lucktype: f.name,
      text: f.text[0],
      image: img
    };
  },
  methods: {
    onIconClicked: function() {
      Alert.alert("운세 선택", "오늘의 운세는 어떤가요?", [
        {
          text: "재물운",
          onPress: () => (lucktype = "재물운")
        },
        {
          text: "사업운",
          onPress: () => (lucktype = "사업운")
        },
        {
          text: "연애운",
          onPress: () => (lucktype = "연애운")
        },
        {
          text: "사랑운",
          onPress: () => (lucktype = "사랑운")
        }
      ]);
    }
  }
};
</script>