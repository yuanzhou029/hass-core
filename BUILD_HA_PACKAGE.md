# 构建 Home Assistant 完整安装包

本指南介绍如何在 Home Assistant Core 项目中构建完整的安装包（包含预编译依赖）。

## 完整安装包的优势

使用预编译依赖的完整安装包相比标准包具有以下优势：

- **安装速度快** - 无需编译依赖包
- **资源占用少** - 不需要编译环境
- **成功率高** - 避免复杂的编译错误
- **兼容性强** - 针对特定平台优化的依赖

## 构建流程

### 1. 使用预编译依赖

在构建完整安装包时，使用您之前构建的预编译依赖：

```bash
# 安装时指定预编译依赖路径
pip install homeassistant-x.x.x-py3-none-any.whl \
    --find-links /path/to/prebuilt/wheels \
    --prefer-binary
```

### 2. 创建整合包

可以将 Home Assistant 主包与预编译依赖打包在一起：

```bash
# 创建包含依赖的发行版
mkdir -p homeassistant-complete/dependencies
cp dist/homeassistant-*.whl homeassistant-complete/
cp /path/to/prebuilt/wheels/*.whl homeassistant-complete/dependencies/
```

### 3. 自动化构建

使用以下自动化脚本构建完整包：

```bash
# 构建主包
python -m build --wheel

# 使用预编译依赖构建完整包
python script/create_complete_package.py
```