#!/usr/bin/env python3
"""
构建 Home Assistant 完整安装包的脚本
整合预编译依赖以加速安装
"""

import os
import subprocess
import shutil
import sys
from pathlib import Path

def build_ha_complete_package():
    """
    构建包含预编译依赖的 Home Assistant 完整包
    """
    print("构建 Home Assistant 完整安装包...")

    # 确保在 Home Assistant 根目录
    if not Path("setup.py").exists() and not Path("pyproject.toml").exists():
        print("错误: 当前目录不是 Home Assistant 项目根目录")
        return False

    # 构建主包
    print("1. 构建 Home Assistant 主包...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "build"], check=True)
        subprocess.run([sys.executable, "-m", "build", "--wheel", "--outdir", "dist"], check=True)
        print("   ✓ 主包构建成功")
    except subprocess.CalledProcessError as e:
        print(f"   ✗ 主包构建失败: {e}")
        return False

    # 查找构建的主包
    dist_path = Path("dist")
    ha_wheel = next(dist_path.glob("homeassistant-*-py3-none-any.whl"), None)
    if not ha_wheel:
        print("   ✗ 未找到构建的主包")
        return False

    print(f"2. 找到主包: {ha_wheel.name}")

    # 创建完整包目录
    complete_pkg_dir = Path("complete_package")
    complete_pkg_dir.mkdir(exist_ok=True)

    # 复制主包
    shutil.copy2(ha_wheel, complete_pkg_dir / ha_wheel.name)

    print("3. 整合预编译依赖...")
    print("   注意: 请确保您的预编译依赖已准备好")
    print("   可以从 hass-wheels 工具的构建结果中获取")

    # 创建安装说明
    install_script = complete_pkg_dir / "INSTALL.md"
    install_script.write_text(f"""
# Home Assistant 完整安装包

## 安装命令

```bash
# 使用预编译依赖安装
pip install {ha_wheel.name} \\
    --find-links dependencies/ \\
    --prefer-binary
```

## 包含组件

- Home Assistant 核心包: {ha_wheel.name}
- 预编译依赖包: 需要从 hass-wheels 工具获取
""")

    print(f"4. 完整包已创建: {complete_pkg_dir.absolute()}")
    print("   请将预编译依赖放入 dependencies/ 目录")
    return True


if __name__ == "__main__":
    print("Home Assistant 完整安装包构建工具")
    print("=" * 50)

    build_ha_complete_package()