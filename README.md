---
title: Flask
description: A popular minimal server framework for Python
tags:
  - python
  - flask
---

# Python Flask Example

This is a [Flask](https://flask.palletsprojects.com/en/1.1.x/) app that serves a simple JSON response.

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/zUcpux)

## ✨ Features

- Python
- Flask

## 💁‍♀️ How to use

- Install Python requirements `pip install -r requirements.txt`
- Start the server for development `python3 main.py`

## 用于代理请求，主要为了请求openai而写

## Postman请求示例：
> curl --location --request POST 'https://xx.xxx.com/message' \
--header 'Content-Type: application/json' \
--data-raw '{
				"url": "https://api.openai.com/v1/chat/completions",
				"openaikey": "sk-51p0ZeNGqyJ7Vh6jgFG0T3BlbkFJN9K9BsI05SA9xxx",
				"msg": {
					"messages": [{"role":"user","content":"测试"},{"role":"user","content":"测试"},{"role":"user","content":"测试"}],
					"model": "gpt-3.5-turbo"
				}
}'