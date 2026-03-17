# 如何创建 Home Assistant 完整安装包

## 概述

Home Assistant 完整安装包包含：
1. Home Assistant 核心包（homeassistant-x.x.x-py3-none-any.whl）
2. 预编译依赖包（使用您构建的 wheels 工具）

## 创建完整安装包的步骤

### 步骤 1: 构建依赖包
使用您的 hass-wheels 工具构建常用的依赖包：
- 运行 `.github/workflows/wheels.yml` 工作流
- 获取构建完成的 wheel 文件

### 步骤 2: 构建主包
在 core 目录下构建 Home Assistant 主包：
```bash
python -m build --wheel
```

### 步骤 3: 整合安装包
使用以下命令整合两种包：
```bash
python script/build_complete_package.py
```

## 使用预编译依赖安装

获得完整包后，可通过以下命令安装：

```bash
# 安装主包并使用预编译依赖
pip install homeassistant-x.x.x-py3-none-any.whl \
    --find-links /path/to/dependencies/ \
    --prefer-binary
```

## 自动化工作流

您也可以扩展 `.github/workflows/wheels.yml` 工作流来自动构建完整安装包：

```yaml
# 在现有 wheels 工作流基础上添加
build_complete_package:
  name: Build complete package with precompiled dependencies
  needs: [core, integrations]
  runs-on: ubuntu-latest
  steps:
    - name: Checkout repository
      uses: actions/checkout@v6.0.2
      
    - name: Download built wheels
      uses: actions/download-artifact@v8.0.0
      with:
        pattern: core-wheels-*
        path: dependencies/
        
    - name: Build main package
      run: |
        pip install build
        python -m build --wheel
        
    - name: Create complete package
      run: python script/build_complete_package.py
      
    - name: Upload complete package
      uses: actions/upload-artifact@v4.3.6
      with:
        name: homeassistant-complete
        path: complete_package/
```

## 优势

使用完整安装包相比传统安装的优势：
- 安装时间缩短 70-90%
- 无需编译环境
- 避免编译错误
- 提高安装成功率