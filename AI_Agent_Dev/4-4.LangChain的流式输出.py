from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model="qwen-max")

# 通过stream方法获得流式输出
res = model.stream(input="你是谁？")

for chunk in res:
    print(chunk, end="", flush=True) # flush=True立刻刷新缓冲区

# Ollama
# from langchain_ollama import OllamaLLM
#
# model = OllamaLLM(model="qwen3:4b")
#
# res = model.stream(input="你是谁？")
#
# for chunk in res:
#     print(chunk, end="", flush=True)
