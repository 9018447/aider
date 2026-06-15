import json
from pathlib import Path

DEFAULT_LOCATIONS = [
    ".aider/tools.json",  # 项目级（优先）
    "~/.aider/tools.json",  # 全局级（回退）
]


def load_tools_config():
    """加载工具配置，项目级覆盖全局级。返回 dict 或 None。"""
    for loc in DEFAULT_LOCATIONS:
        path = Path(loc).expanduser()
        if path.is_file():
            try:
                return json.loads(path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                pass
    return None


def get_tools_summary(config):
    """从配置生成简短的工具清单字符串，用于启动时展示。"""
    if not config or "tools" not in config:
        return ""
    lines = []
    for name, info in config["tools"].items():
        if info.get("enabled", True):
            desc = info.get("description", "")
            lines.append(f"  {name} ({info.get('type', 'cli')}): {desc}")
    return "\n".join(lines)
