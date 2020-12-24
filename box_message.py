main_menu = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:20",
        "aspectMode": "cover",
        "url": "https://i.imgur.com/tBDRxae.png"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "message",
              "text": "飼料",
              "label": "關於飼料"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:20",
        "aspectMode": "cover",
        "url": "https://i.imgur.com/ndbrXCp.png"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "message",
              "text": "水",
              "label": "關於喝水"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:20",
        "aspectMode": "cover",
        "url": "https://i.imgur.com/G44rKz6.png"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "message",
              "text": "草",
              "label": "關於吃草"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:20",
        "aspectMode": "cover",
        "url": "https://i.imgur.com/pozvDER.png"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "message",
              "text": "知識",
              "label": "兔兔の小知識"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:20",
        "aspectMode": "cover",
        "url": "https://i.imgur.com/f78NKC4.png"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "message",
              "text": "ptt",
              "label": "看看ptt兔版都在討論什麼"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:20",
        "aspectMode": "cover",
        "url": "https://i.imgur.com/u0xiL42.png"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "message",
              "text": "fsm",
              "label": "fsm圖片"
            }
          }
        ]
      }
    }
  ]
}

water_menu = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://i.imgur.com/Ihu9bn9.png",
    "size": "full",
    "aspectRatio": "20:20",
    "aspectMode": "cover"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "weight": "bold",
        "size": "md",
        "text": "在這裡你可以了解你的兔兔一天需",
        "contents": []
      },
      {
        "type": "text",
        "text": "要喝多少水以及關於兔兔喝水的注",
        "weight": "bold",
        "size": "md"
      },
      {
        "type": "text",
        "text": "意事項哦 !",
        "size": "md",
        "weight": "bold"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "請選擇功能",
                "color": "#666666",
                "size": "lg",
                "flex": 5
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "text": "水量",
          "label": "兔兔一天的需水量"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "text": "注意事項",
          "label": "兔兔喝水的注意事項"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "text": "主選單",
          "label": "主選單"
        }
      },
      {
        "type": "spacer",
        "size": "sm"
      }
    ],
    "flex": 0
  }
}

show_water = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://i.imgur.com/CJLbSXA.png",
    "size": "full",
    "aspectRatio": "20:20",
    "aspectMode": "cover"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "你家的兔兔一天至少要喝",
        "weight": "bold",
        "size": "lg"
      },
      {
        "type": "text",
        "text": "100.0 毫升的水哦 !",
        "weight": "bold",
        "size": "lg"
      },
      {
        "type": "text",
        "text": "不夠的話快幫他補充水分吧",
        "weight": "bold",
        "size": "lg"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "兔兔喝水的注意事項",
          "text": "注意事項"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "主選單",
          "text": "主選單"
        }
      }
    ],
    "flex": 0
  }
}

feed_menu ={
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://i.imgur.com/mZFwTcA.png",
    "size": "full",
    "aspectRatio": "20:20",
    "aspectMode": "cover"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "weight": "bold",
        "size": "md",
        "text": "在這裡你可以知道兔兔一天需要吃",
        "contents": []
      },
      {
        "type": "text",
        "text": "多少飼料或是飼料沒了可以去哪買",
        "weight": "bold",
        "size": "md"
      },
      {
        "type": "text",
        "text": "哦!",
        "size": "md",
        "weight": "bold"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "請選擇功能",
                "color": "#666666",
                "size": "lg",
                "flex": 5
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "text": "飼料量",
          "label": "我家兔兔一天要吃多少飼料"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "text": "地點",
          "label": "兔兔飼料沒了該去哪買呢"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "text": "注意事項",
          "label": "兔兔吃飼料的注意事項"
        }
      },      
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "text": "主選單",
          "label": "主選單"
        }
      }
    ],
    "flex": 0
  }
}

show_feed = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://i.imgur.com/Z22TBc1.png",
    "size": "full",
    "aspectRatio": "20:20",
    "aspectMode": "cover"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "你家的兔兔適合什麼飼料",
        "weight": "bold",
        "size": "lg"
      },
      {
        "type": "text",
        "text": "一天可以吃約",
        "weight": "bold",
        "size": "lg"
      },
      {
        "type": "text",
        "text": "100.0 ~ 200.0公克的飼料哦 !",
        "weight": "bold",
        "size": "lg"
      },
      {
        "type": "text",
        "text": "大約是 1~2 匙的量",
        "weight": "bold",
        "size": "lg"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "兔兔吃飼料的注意事項",
          "text": "注意事項"
        }
      },      
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "主選單",
          "text": "主選單"
        }
      }
    ],
    "flex": 0
  }
}

grass_menu = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://i.imgur.com/rkCAeQT.png",
    "size": "full",
    "aspectRatio": "20:20",
    "aspectMode": "cover"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "weight": "bold",
        "size": "md",
        "text": "在這裡可以知道你的的兔兔適合",
        "contents": []
      },
      {
        "type": "text",
        "text": "吃什麼草唷!當然還有餵草時的注",
        "weight": "bold",
        "size": "md"
      },
      {
        "type": "text",
        "text": "意事項啦~別錯過",
        "size": "md",
        "weight": "bold"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "請選擇功能",
                "color": "#666666",
                "size": "lg",
                "flex": 5
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "text": "哪種草",
          "label": "我家兔兔適合吃哪種草"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "text": "注意事項",
          "label": "兔兔吃草時的注意事項"
        }
      },      
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "text": "主選單",
          "label": "主選單"
        }
      },
      {
        "type": "spacer",
        "size": "sm"
      }
    ],
    "flex": 0
  }
}

show_grass = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://i.imgur.com/5E1FSwm.png",
    "size": "full",
    "aspectRatio": "20:20",
    "aspectMode": "cover"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "你家的兔兔適合吃的是",
        "weight": "bold",
        "size": "lg"
      },
      {
        "type": "text",
        "text": "什麼草哦",
        "weight": "bold",
        "size": "lg"
      },
      {
        "type": "text",
        "text": " ",
        "weight": "bold",
        "size": "lg"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "兔兔吃草的注意事項",
          "text": "注意事項"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "主選單",
          "text": "主選單"
        }
      }
    ],
    "flex": 0
  }
}

about_rabbit_menu = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://i.imgur.com/qlDLcTc.png",
    "size": "full",
    "aspectRatio": "20:20",
    "aspectMode": "cover"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "weight": "bold",
        "size": "md",
        "text": "在這裡你可以知道許多你可能",
        "contents": []
      },
      {
        "type": "text",
        "text": "不知道的有關兔兔小知識哦",
        "weight": "bold",
        "size": "md"
      },
      {
        "type": "text",
        "text": "快來看看",
        "size": "md",
        "weight": "bold"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "請選擇項目",
                "color": "#666666",
                "size": "lg",
                "flex": 5
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "text": "飲食",
          "label": "有關兔兔飲食"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "text": "肢體語言",
          "label": "兔兔的肢體語言"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "text": "冷知識",
          "label": "兔兔冷知識"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "text": "主選單",
          "label": "主選單"
        }
      },
      {
        "type": "spacer",
        "size": "sm"
      }
    ],
    "flex": 0
  }
}

show_ptt = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/eWcNuIR.jpg",
        "size": "full",
        "aspectRatio": "20:20",
        "aspectMode": "cover"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "uri": "http://linecorp.com/",
              "label": "action"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/eWcNuIR.jpg",
        "size": "full",
        "aspectRatio": "20:20",
        "aspectMode": "cover"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://linecorp.com/"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/eWcNuIR.jpg",
        "size": "full",
        "aspectRatio": "20:20",
        "aspectMode": "cover"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://linecorp.com/"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/eWcNuIR.jpg",
        "size": "full",
        "aspectRatio": "20:20",
        "aspectMode": "cover"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://linecorp.com/"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/eWcNuIR.jpg",
        "size": "full",
        "aspectRatio": "20:20",
        "aspectMode": "cover"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://linecorp.com/"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/J9UAtLk.png",
        "size": "full",
        "aspectRatio": "20:20",
        "aspectMode": "cover"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "回主選單",
              "text": "主選單"
            }
          }
        ]
      }
    }
  ]
}

show_fsm = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://i.imgur.com/jNLAh1l.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover"
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "點我查看fsm圖片",
          "uri": "https://i.imgur.com/mjphDWB.png"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "回主選單",
          "text": "主選單"
        }
      },
      {
        "type": "spacer",
        "size": "sm"
      }
    ],
    "flex": 0
  }
}
