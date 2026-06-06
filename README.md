# 🎨 Theme Tools

AI主题工具，支持主题生成、配色、样式。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🎨 主题生成
- 🎨 CSS变量生成
- ⚙️ Tailwind配置
- 🎨 Material Design主题
- 🌙 暗色模式生成
- 💡 主题建议

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from theme_tools import create_tools

tools = create_tools()

# 生成主题
theme = tools.generate_theme("科技感", "tailwind")

# CSS变量
css = tools.generate_css_variables(theme)

# Tailwind配置
tailwind = tools.generate_tailwind_config(theme)

# Material主题
material = tools.generate_material_theme("#3a7bd5", "light")

# 暗色模式
dark = tools.generate_dark_mode(light_theme)

# 主题建议
suggestion = tools.suggest_theme("专业、现代、可信赖")
```

## 📁 项目结构

```
theme-tools/
├── tools.py       # 主题工具核心
└── README.md
```

## 📄 许可证

MIT License
