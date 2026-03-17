# 发布到 GitHub Releases

本指南说明如何使用更新后的 wheels 工作流将构建的文件发布到 GitHub Releases。

## 功能说明

更新后的 `.github/workflows/wheels.yml` 工作流包含一个新作业 `publish-to-github-releases`，它会：

1. 收集所有构建的 wheel 包（包括核心依赖和集成依赖）
2. 将 Home Assistant 主包与预编译依赖整合
3. 发布到 GitHub Releases 中

## 触发方式

- **手动触发**：在 Actions 页面手动运行工作流
- **仅限仓库所有者**：由于安全原因，只有仓库所有者（yuanzhou029）可以发布到 Releases

## 发布内容

每次发布包含：

- 所有预编译的 wheel 文件
- Home Assistant 主包
- 完整安装包（包含依赖的整合包）
- ASSETS_SUMMARY.md - 包含发布内容的摘要

## 使用步骤

1. 确保工作流成功执行了构建作业（core, integrations, build-complete-package）
2. 在 GitHub Actions 页面找到 "Build Core Wheels with Custom Wheels Tool" 工作流
3. 点击 "Run workflow" 按钮手动触发
4. 选择使用 `workflow_dispatch` 事件运行
5. 工作流完成后，前往 Releases 页面查看新发布的版本

## 注意事项

- 发布需要 `contents: write` 权限
- 只有在 `workflow_dispatch` 事件时才会执行发布作业
- 发布的标签格式为 `v{VERSION}_deps`
- 如果无法提取版本号，将使用时间戳作为版本标识

## 权限配置

工作流中已配置适当的权限：

```yaml
permissions:
  contents: write  # 用于创建发布
```

确保您的 GitHub 个人访问令牌具有适当的权限以创建 Releases。