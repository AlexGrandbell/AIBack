# AI 后端服务说明

本项目是一个基于 Python Flask 的单文件后端服务，主要负责代理和转发 AI 模型请求，提供流式响应功能。适用于配合前端进行 AI 题目生成和对话交互。

## 依赖环境

- Python 3.7 及以上版本
- 依赖库安装：
  ```bash
  pip install flask requests flask-cors
  ```

## 配置说明

- 请在文件中找到 `API_KEY` 变量，替换为你从 DeepSeek 官网购买或申请的 API 密钥：
  ```python
  API_KEY = "你的API密钥"
  ```

## 运行方式

1. 进入项目所在目录  
2. 运行服务：
   ```bash
   python DeepCraftBack.py
   ```
3. 服务默认监听地址和端口：
   ```
   http://0.0.0.0:5110
   ```

## 功能说明

- 提供 `/chat` POST 接口，接收前端传来的聊天请求  
- 代理请求至 DeepSeek AI 服务，并以 SSE 形式流式返回数据  
- 支持跨域请求，方便前端调用

## 注意事项

- 确保服务器网络环境能访问 DeepSeek API  
- API_KEY 请妥善保管，不要泄露  
- 生产环境建议关闭 `debug` 模式

---

如有疑问或需要扩展功能，欢迎反馈。
