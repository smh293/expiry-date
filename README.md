# expiry-date
一个可以通过输入生成日期和保质期推测过期日的程序
# 日期和保质期推测过期日程序

一个简单的Python程序，可以通过输入当前日期和保质期来推测过期日。

## 功能特点

- 📅 输入当前日期（支持手动输入或使用今天日期）
- 📦 输入保质期（支持天、周、月、年单位）
- ⏰ 自动计算过期日期
- 📊 显示剩余天数
- ⚠️ 提供过期提醒

## 使用方法

### 在线运行
1. 在GitHub Codespaces中打开本项目
2. 运行 `python main.py`
3. 按照提示输入信息

### 获取Windows可执行文件
1. 前往 [Actions](https://github.com/你的用户名/expiry-date-calculator/actions) 页面
2. 选择最新的工作流运行
3. 在"Artifacts"部分下载 `过期日计算器-Windows`

## 构建说明

程序使用GitHub Actions自动构建Windows可执行文件，无需手动操作。

## 技术栈

- Python 3.9+
- PyInstaller (用于打包)
- GitHub Actions (用于CI/CD)

## 许可证

MIT License