# 阿里云通义千问大语言模型的访问（langchain_community包）
from langchain_community.llms.tongyi import Tongyi

# 显式设置 api_key（推荐从环境变量读取，避免硬编码）
# 如果已经在 .zshrc 设了 DASHSCOPE_API_KEY，这里可以不写
# tongyi_llm = Tongyi(model="qwen-max", dashscope_api_key=os.getenv("DASHSCOPE_API_KEY"))

# 简洁版（如果已设环境变量）
# 不用qwen3-max，因为qwen3-max是聊天模型，qwen-max是大语言模型
model = Tongyi(model="qwen-max")

# 调用invoke向模型提问
res = model.invoke(input="你是谁？")

print(res)