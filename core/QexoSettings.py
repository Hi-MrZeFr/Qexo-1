import json
import random

QEXO_VERSION = "1.7.0"

ALL_SETTINGS = [  # [名称, 默认值, 是否在尝试修复时重置, 简介]
    ["ABBRLINK_ALG", "crc16", False, "短链接算法"],
    ["ABBRLINK_REP", "dec", False, "短链接格式dec/hex"],
    ["CDN_PREV", "https://npm.elemecdn.com/", True, "调用NPM的CDN前缀"],
    ["GH_REPO", "", False, "Github用户名"],
    ["GH_REPO_BRANCH", "", False, "仓库分支"],
    ["GH_REPO_PATH", "", False, "仓库路径"],
    ["GH_TOKEN", "", False, "Github密钥"],
    ["IMG_API", "", False, "图床API地址"],
    ["IMG_CUSTOM_BODY", "", False, "图床自定义请求主体"],
    ["IMG_CUSTOM_HEADER", "", False, "图床自定义请求头"],
    ["IMG_CUSTOM_URL", "", False, "图床自定义链接前缀"],
    ["IMG_JSON_PATH", "", False, "图床JSON路径"],
    ["IMG_POST", "", False, "图床图片请求名"],
    ["IMG_TYPE", "", False, "图床类别"],
    ["INIT", "2", False, "初始化标识"],
    ["QEXO_ICON",
     "https://npm.elemecdn.com/qexo-static@1.4.0/assets/img/brand/favicon.ico",
     False, "站点ICON"],
    ["QEXO_LOGO",
     "https://npm.elemecdn.com/qexo-static@1.4.0/assets/img/brand/qexo.png",
     False, "站点LOGO"],
    ["QEXO_NAME", "Hexo管理面板", False, "站点名"],
    ["QEXO_SPLIT", "-", False, "站点分隔符"],
    ["S3_ACCESS_KEY", "", False, "S3权限密钥"],
    ["S3_BUCKET", "", False, "S3桶"],
    ["S3_ENDPOINT", "", False, "S3边缘节点"],
    ["S3_KEY_ID", "", False, "S3密钥ID"],
    ["S3_PATH", "", False, "S3上传路径"],
    ["S3_PREV_URL", "", False, "S3链接前缀"],
    ["VDITOR_EMOJI",
     json.dumps({"微笑": "🙂", "撇嘴": "😦", "色": "😍", "发呆": "😍", "得意": "😎",
                 "流泪": "😭", "害羞": "😊", "闭嘴": "😷", "睡": "😴",
                 "大哭 ": "😡", "尴尬": "😡", "发怒": "😛", "调皮": "😀", "呲牙": "😯",
                 "惊讶": "🙁", "难过": "😎", "酷": "😨", "冷汗": "😱", "抓狂": "😵", "吐 ": "😋",
                 "偷笑": "☺", "愉快": "🙄", "白眼": "🙄", "傲慢": "😋", "饥饿": "😪", "困": "😫",
                 "惊恐": "😓", "流汗": "😃", "憨笑": "😃", "悠闲 ": "😆", "奋斗": "😆",
                 "咒骂": "😆", "疑问": "😆", "嘘": "😵", "晕": "😆", "疯了": "😆", "衰": "😆",
                 "骷髅": "💀", "敲打": "😬", "再见 ": "😘", "擦汗": "😆", "抠鼻": "😆",
                 "鼓掌": "👏", "糗大了": "😆", "坏笑": "😆", "左哼哼": "😆", "右哼哼": "😆",
                 "哈欠": "😆", "鄙视": "😆", "委屈 ": "😆", "快哭了": "😆", "阴险": "😆",
                 "亲亲": "😘", "吓": "😓", "可怜": "😆", "菜刀": "🔪", "西瓜": "🍉", "啤酒": "🍺",
                 "篮球": "🏀", "乒乓 ": "⚪", "咖啡": "☕", "饭": "🍚", "猪头": "🐷", "玫瑰": "🌹",
                 "凋谢": "🌹", "嘴唇": "👄", "爱心": "💗", "心碎": "💔", "蛋糕": "🎂", "闪电 ": "⚡",
                 "炸弹": "💣", "刀": "🗡", "足球": "⚽", "瓢虫": "🐞", "便便": "💩", "月亮": "🌙",
                 "太阳": "☀", "礼物": "🎁", "拥抱": "🤗", "强 ": "👍", "弱": "👎", "握手": "👍",
                 "胜利": "✌", "抱拳": "✊", "勾引": "✌", "拳头": "✊", "差劲": "✌", "爱你": "✌",
                 "NO": "✌", "OK": "🙂", "嘿哈": "🙂", "捂脸": "🙂", "奸笑": "🙂", "机智": "🙂",
                 "皱眉": "🙂", "耶": "🙂", "吃瓜": "🙂", "加油": "🙂", "汗": "🙂", "天啊": "👌",
                 "社会社会": "🙂", "旺柴": "🙂", "好的": "🙂", "哇": "🙂"}), True, "自定义表情"],
    ["WEBHOOK_APIKEY", ''.join(random.choice("qwertyuiopasdfghjklzxcvbnm1234567890")
                               for x in range(12)), False, "API密钥"],
    ["VERCEL_TOKEN", "", False, "Vercel密钥"],
    ["PROJECT_ID", "", False, "Qexo项目ID"],
    ["ALLOW_FRIEND", "否", False, "是否允许友链申请 是/否"],
    ["LAST_LOGIN", "", True, "博主最后上线时间(无需更改)"],
    ["FTP_HOST", "", False, "FTP服务器"],
    ["FTP_PORT", "", False, "FTP端口"],
    ["FTP_USER", "", False, "FTP用户名"],
    ["FTP_PASS", "", False, "FTP密码"],
    ["FTP_PATH", "", False, "FTP文件上传地址"],
    ["FTP_PREV_URL", "", False, "FTP图床链接"],
    ["ONEPUSH", "", False, "OnePush消息通知"],
    ["STATISTIC_ALLOW", "否", False, "是否开启统计功能 是/否"],
    ["STATISTIC_DOMAINS", "", False, "统计安全域名 英文半角逗号间隔"],
]
