# Voice Reply

MiniMax speech-2.8-hd TTS voice reply skill. Generate and play speech audio after every text reply via `afplay`.

## 功能概述

在 AI 助手每次文字回复后，自动调用 MiniMax speech-2.8-hd 生成语音并通过系统播放器（macOS `afplay`）从电脑喇叭直接播出，无需点击、无需手动播放。

## 核心特性

- **高清音质**：MiniMax speech-2.8-hd 模型，支持 40 种中文音色
- **即时播报**：生成后立即通过 `afplay` 播放
- **即装即用**：无需额外依赖（requests 库，macOS 内置 afplay）
- **隐私优先**：API Key 可配置，不上传任何用户数据

## 实现方式

```
用户文字回复
    ↓
AI 生成文字内容
    ↓
调用 voice_reply.py 生成 MP3 音频
    ↓
afplay 从系统喇叭播放
```

### 技术细节

- **TTS API**：MiniMax T2A v2 HTTP 接口
- **模型**：speech-2.8-hd（高清语音）
- **音频格式**：MP3，32000Hz，128kbps
- **播放**：macOS 内置 `/usr/bin/afplay`，无依赖
- **代理**：直连 `api.minimaxi.com`，无需代理（若网络不通可走代理）

## 安装

### 1. 克隆仓库

```bash
git clone https://github.com/Wh1t3co1azZ/voice-reply.git
cd voice-reply
```

### 2. 安装 Python 依赖

```bash
pip3 install requests --user
```

### 3. 配置 API Key

编辑 `voice_reply.py`，替换 `DEFAULT_API_KEY` 为你的 MiniMax API Key：

```python
DEFAULT_API_KEY = "your-minimax-api-key-here"
```

获取 API Key：https://platform.minimaxi.com/

## 使用方法

### 命令行

```bash
# 基本用法
python3 voice_reply.py "你好，这是语音测试" /tmp/test.mp3

# 指定音色
python3 voice_reply.py "你好" /tmp/test.mp3 female-yujie

# 指定语速（0.5-2.0）
python3 voice_reply.py "快速播报" /tmp/test.mp3 female-shaonv 1.5
```

### Python API

```python
from voice_reply import speak

# 默认音色（少女音色）
speak("义父好，这是一条语音播报测试。")

# 指定音色
speak("你好，这是一条御姐音色的测试。", voice_id="female-yujie")

# 指定语速
speak("快速播报测试", voice_id="male-qn-badao", speed=1.5)

# 不自动播放（生成文件）
speak("只生成文件", play=False, out_path="/tmp/custom.mp3")
```

## 音色列表

完整音色列表及说明：https://platform.minimaxi.com/docs/faq/system-voice-id

### 常用音色速查

| Voice ID | 名称 | 适用场景 |
|----------|------|---------|
| `female-shaonv` | 少女音色 | 默认，柔和亲切 |
| `female-shaonv-jingpin` | 少女音色-beta | 增强版少女音 |
| `female-yujie` | 御姐音色 | 成熟稳重 |
| `female-tianmei` | 甜美女性音色 | 温柔甜美 |
| `male-qn-jingying` | 精英青年音色 | 专业正式 |
| `male-qn-badao` | 霸道青年音色 | 强势有力 |
| `male-qn-daxuesheng` | 青年大学生音色 | 青春活力 |

### 更多音色

| 音色ID | 名称 |
|--------|------|
| `female-chengshu` | 成熟女性音色 |
| `female-chengshu-jingpin` | 成熟女性音色-beta |
| `female-tianmei-jingpin` | 甜美女性音色-beta |
| `male-qn-qingse` | 青涩青年音色 |
| `male-qn-jingying-jingpin` | 精英青年音色-beta |
| `male-qn-badao-jingpin` | 霸道青年音色-beta |
| `male-qn-daxuesheng-jingpin` | 青年大学生音色-beta |
| `Chinese (Mandarin)_Reliable_Executive` | 沉稳高管 |
| `Chinese (Mandarin)_News_Anchor` | 新闻女声 |
| `Chinese (Mandarin)_Mature_Woman` | 傲娇御姐 |
| `Chinese (Mandarin)_Unrestrained_Young_Man` | 不羁青年 |
| `Chinese (Mandarin)_Gentleman` | 温润男声 |
| `Chinese (Mandarin)_Kind-hearted_Antie` | 热心大婶 |
| `Chinese (Mandarin)_Humorous_Elder` | 搞笑大爷 |
| `Chinese (Mandarin)_HK_Flight_Attendant` | 港普空姐 |
| `Arrogant_Miss` | 嚣张小姐 |
| `Robot_Armor` | 机械战甲 |
| `clever_boy` | 聪明男童 |
| `cute_boy` | 可爱男童 |
| `lovely_girl` | 萌萌女童 |
| `cartoon_pig` | 卡通猪小琪 |
| `bingjiao_didi` | 病娇弟弟 |
| `junlang_nanyou` | 俊朗男友 |
| `chunzhen_xuedi` | 纯真学弟 |
| `lengdan_xiongzhang` | 冷淡学长 |
| `badao_shaoye` | 霸道少爷 |
| `tianxin_xiaoling` | 甜心小玲 |
| `qiaopi_mengmei` | 俏皮萌妹 |
| `wumei_yujie` | 妩媚御姐 |
| `diadia_xuemei` | 嗲嗲学妹 |
| `danya_xuejie` | 淡雅学姐 |

## 参数说明

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `text` | str | 必填 | 要合成的文字内容 |
| `voice_id` | str | `female-shaonv` | 音色ID |
| `speed` | float | 1.0 | 语速，范围 0.5-2.0 |
| `vol` | float | 1.0 | 音量，范围 0-2.0 |
| `pitch` | int | 0 | 音调，范围 -12 到 12 |
| `out_path` | str | `/tmp/tts_output.mp3` | 输出文件路径 |
| `play` | bool | `True` | 是否自动播放 |

## 故障排除

| 问题 | 原因 | 解决方案 |
|------|------|---------|
| `Connection refused` | 网络不通 | 尝试配置代理或检查网络 |
| `Token error` | API Key 无效或过期 | 检查或更换 API Key |
| 无音频播放 | afplay 路径问题 | 确认 macOS 系统，afplay 为内置工具 |
| `Empty audio` | 文字为空或语言不支持 | 检查输入文字 |

## 文件结构

```
voice-reply/
├── README.md             # 本文件
└── voice_reply.py        # 核心 TTS 脚本
```

## 开源许可

MIT License

## 相关链接

- MiniMax 平台：https://platform.minimaxi.com/
- 音色列表：https://platform.minimaxi.com/docs/faq/system-voice-id
- GitHub 仓库：https://github.com/Wh1t3co1azZ/voice-reply
