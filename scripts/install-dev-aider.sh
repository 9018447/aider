#!/usr/bin/env bash
set -euo pipefail

echo "=== 清理旧版 aider ==="

# 删除通过 pip/uv 安装的 aider 包
if uv tool list 2>/dev/null | grep -q aider-chat; then
    echo "-> 移除 uv tool 安装的 aider..."
    uv tool uninstall aider-chat 2>/dev/null || true
fi

# 删除当前 venv 中的 aider
if pip show aider-chat &>/dev/null 2>&1; then
    echo "-> 卸载 pip 安装的 aider..."
    pip uninstall aider-chat -y 2>/dev/null || true
fi

# 删除任何残留的 entry point
rm -f "$HOME/.local/bin/aider" 2>/dev/null || true



echo ""
echo "=== 安装开发版 aider ==="
PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

uv tool install --editable "$PROJECT_DIR[browser,help]"

echo ""
echo "=== 验证 ==="
if command -v aider &>/dev/null; then
    echo "aider 安装成功: $(which aider)"
    aider --version 2>/dev/null || true
else
    echo "WARNING: aider 不在 PATH 中"
    echo "请将 \$HOME/.local/bin 添加到 PATH"
fi
