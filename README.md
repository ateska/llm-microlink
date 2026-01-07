# llm-microlink

`llm-microlink` is an LLM proxy that connects [large language models](https://en.wikipedia.org/wiki/Large_language_model) to your [microservice](https://en.wikipedia.org/wiki/Microservices) ecosystem, enabling seamless **tool calling**.
It discovers tools advertised by your services, passes them to the LLM, executes tool calls via REST APIs, and feeds results back into the conversation — all automatically.

## Key Features

* **Universal LLM Support** — Connect to local models (vLLM, TensorRT-LLM) or frontier APIs (OpenAI, Anthropic Claude) through a unified interface
* **Dynamic Tool Discovery** — Microservices register their capabilities via [Apache Zookeeper](https://en.wikipedia.org/wiki/Apache_ZooKeeper); `llm-microlink` picks them up automatically
* **Native Tool Calling** — Leverages built-in function calling capabilities of modern LLMs for reliable, structured interactions

## Built With

* [Python](https://www.python.org) & [ASAB](https://github.com/TeskaLabs/asab) microservice framework
* [Apache Zookeeper](https://en.wikipedia.org/wiki/Apache_ZooKeeper) for tools & service discovery

