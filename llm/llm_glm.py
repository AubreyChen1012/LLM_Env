from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    temperature=0.95,
    model="glm-4-flash",
    openai_api_key="7d7dd0de20661b8280e7b6b419fd577e.Oi6RZQJwOkmOgw8o",
    openai_api_base="https://open.bigmodel.cn/api/paas/v4/"
)
