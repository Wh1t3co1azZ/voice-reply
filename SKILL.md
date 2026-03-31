---
name: voice-reply
version: 1.0.0
description: MiniMax speech-2.8-hd TTS voice reply. Generate and play speech audio after every text reply.
homepage: https://github.com/Wh1t3co1azZ/voice-reply
emoji: 🗣️
---

# Voice Reply

MiniMax speech-2.8-hd TTS voice reply skill. After every text reply, generates speech audio and plays it through the system speaker using `afplay`.

## Requirements

- Python 3 with `requests` library
- MiniMax API Key (`MINIMAX_API_KEY` env var or inline in script)
- `afplay` (macOS built-in) for audio playback
- No proxy needed (direct connection to `api.minimaxi.com`)

## Usage

### One-line command

```bash
PYTHONPATH=/path/to/site-packages python3 /path/to/voice_reply.py "文字内容" [output.mp3]
```

### Python API

```python
from voice_reply import speak
speak("义父好，这是一条语音播报测试。", voice_id="female-shaonv", out_path="/tmp/tts.mp3")
```

### Voice IDs (Chinese Mandarin)

| Voice ID | Name | Description |
|----------|------|-------------|
| `female-shaonv` | 少女音色 | Young female (default) |
| `female-shaonv-jingpin` | 少女音色-beta | Enhanced young female |
| `female-yujie` | 御姐音色 | Mature female |
| `female-yujie-jingpin` | 御姐音色-beta | Enhanced mature female |
| `female-chengshu` | 成熟女性音色 | Senior female |
| `female-chengshu-jingpin` | 成熟女性音色-beta | Enhanced senior female |
| `female-tianmei` | 甜美女性音色 | Sweet female |
| `female-tianmei-jingpin` | 甜美女性音色-beta | Enhanced sweet female |
| `male-qn-qingse` | 青涩青年音色 | Shy young male |
| `male-qn-qingse-jingpin` | 青涩青年音色-beta | Enhanced shy young male |
| `male-qn-jingying` | 精英青年音色 | Elite young male |
| `male-qn-jingying-jingpin` | 精英青年音色-beta | Enhanced elite young male |
| `male-qn-badao` | 霸道青年音色 | Dominant young male |
| `male-qn-badao-jingpin` | 霸道青年音色-beta | Enhanced dominant young male |
| `male-qn-daxuesheng` | 青年大学生音色 | College student male |
| `male-qn-daxuesheng-jingpin` | 青年大学生音色-beta | Enhanced college student male |
| `Chinese (Mandarin)_Reliable_Executive` | 沉稳高管 | Reliable executive |
| `Chinese (Mandarin)_News_Anchor` | 新闻女声 | News anchor female |
| `Chinese (Mandarin)_Mature_Woman` | 傲娇御姐 | Tsundere female |
| `Chinese (Mandarin)_Unrestrained_Young_Man` | 不羁青年 | Unrestrained young male |
| `Chinese (Mandarin)_Gentleman` | 温润男声 | Gentle male |
| `Chinese (Mandarin)_Kind-hearted_Antie` | 热心大婶 | Kind-hearted aunt |
| `Chinese (Mandarin)_Humorous_Elder` | 搞笑大爷 | Humorous elder |
| `Chinese (Mandarin)_HK_Flight_Attendant` | 港普空姐 | HK flight attendant |
| `Arrogant_Miss` | 嚣张小姐 | Arrogant miss |
| `Robot_Armor` | 机械战甲 | Robot armor |
| `clever_boy` | 聪明男童 | Clever boy |
| `cute_boy` | 可爱男童 | Cute boy |
| `lovely_girl` | 萌萌女童 | Lovely girl |
| `cartoon_pig` | 卡通猪小琪 | Cartoon pig |
| `bingjiao_didi` | 病娇弟弟 | Yandere little brother |
| `junlang_nanyou` | 俊朗男友 | Handsome boyfriend |
| `chunzhen_xuedi` | 纯真学弟 | Innocent junior male |
| `lengdan_xiongzhang` | 冷淡学长 | Cold senior male |
| `badao_shaoye` | 霸道少爷 | Domineering young master |
| `tianxin_xiaoling` | 甜心小玲 | Sweetheart Xiaoling |
| `qiaopi_mengmei` | 俏皮萌妹 | Witty cute girl |
| `wumei_yujie` | 妩媚御姐 | Glamorous mature female |
| `diadia_xuemei` | 嗲嗲学妹 | Doting junior female |
| `danya_xuejie` | 淡雅学姐 | Elegant senior female |

## Audio Settings

- Format: MP3
- Sample rate: 32000 Hz
- Bitrate: 128000 bps
- Speed: 1.0 (adjustable 0.5–2.0)
- Pitch: 0 (adjustable -12 to 12)

## API Details

- Endpoint: `POST https://api.minimaxi.com/v1/t2a_v2`
- Model: `speech-2.8-hd`
- Auth: Bearer token in `Authorization` header

## Files

```
voice-reply/
├── SKILL.md          # This file
├── scripts/
│   └── voice_reply.py   # Main TTS script
└── references/
    └── voice-list.md    # Voice ID reference
```

## Installation

```bash
# Install requests if needed
pip3 install requests --user

# Test
python3 voice_reply.py "你好，这是语音测试" /tmp/test.mp3 && afplay /tmp/test.mp3
```

## Troubleshooting

- **Connection refused**: Proxy may be blocking. Try without proxy.
- **Token error**: Check API key is valid and has not expired.
- **No audio**: Verify `afplay` works on your system.
- **Empty audio**: Check text is not empty and language is supported.
