"""
Theme Tools - AI主题工具
支持主题生成、配色、样式
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class ThemeTools:
    """
    AI主题工具
    支持：生成、配色、样式
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def generate_theme(self, style: str, framework: str = "tailwind") -> Dict:
        """生成主题"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请生成{style}风格的{framework}主题：

请返回JSON格式：
{{
    "name": "主题名称",
    "colors": {{
        "primary": "#xxx",
        "secondary": "#xxx",
        "accent": "#xxx",
        "background": "#xxx",
        "text": "#xxx"
    }},
    "typography": {{
        "font_family": "字体",
        "font_sizes": {{}}
    }},
    "spacing": {{}},
    "border_radius": {{}},
    "shadows": {{}}
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"theme": content}

    def generate_css_variables(self, theme: Dict) -> str:
        """生成CSS变量"""
        if not self.client:
            return "LLM客户端未配置"

        theme_text = json.dumps(theme, ensure_ascii=False)

        prompt = f"""请根据以下主题生成CSS变量：

{theme_text}

请返回完整的CSS变量定义："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content

    def generate_tailwind_config(self, theme: Dict) -> str:
        """生成Tailwind配置"""
        if not self.client:
            return "LLM客户端未配置"

        theme_text = json.dumps(theme, ensure_ascii=False)

        prompt = f"""请根据以下主题生成Tailwind CSS配置：

{theme_text}

请返回完整的tailwind.config.js："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500
        )

        return response.choices[0].message.content

    def generate_material_theme(self, primary_color: str, style: str = "light") -> str:
        """生成Material Design主题"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成Material Design 3主题：

主色：{primary_color}
风格：{style}

请返回完整的主题配置："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content

    def generate_dark_mode(self, light_theme: Dict) -> Dict:
        """生成暗色模式"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        theme_text = json.dumps(light_theme, ensure_ascii=False)

        prompt = f"""请根据以下亮色主题生成暗色模式：

{theme_text}

请返回JSON格式的暗色主题："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"dark_theme": content}

    def suggest_theme(self, brand_description: str) -> Dict:
        """建议主题"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请根据以下品牌描述建议主题：

{brand_description}

请返回JSON格式：
{{
    "style": "风格",
    "mood": "情绪",
    "colors": ["推荐颜色"],
    "fonts": ["推荐字体"],
    "examples": ["参考案例"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"suggestion": content}


def create_tools(**kwargs) -> ThemeTools:
    """创建主题工具"""
    return ThemeTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("Theme Tools")
    print()

    # 测试
    theme = tools.generate_theme("科技感", "tailwind")
    print(json.dumps(theme, ensure_ascii=False, indent=2))
