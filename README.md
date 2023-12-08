<p align="center">
   <a href="https://github.com/AryanVBw">
<img src="https://github.com/AryanVBW/Private-Ai/releases/download/I1/Bgdark.png" alt="Darkside"></a></p>

</p>

# 🚀 Welcome to Private-AI!

Private-AI is an innovative AI project designed for asking questions about your documents using powerful Large Language Models (LLMs). The unique feature? It works offline, ensuring 100% privacy with no data leaving your environment.

## 🌐 What does Private-AI offer?

- **High-level API:** Abstracts the complexity of a Retrieval Augmented Generation (RAG) pipeline. Handles document ingestion, chat, and completions.
  
- **Low-level API:** For advanced users to implement custom pipelines. Includes features like embeddings generation and contextual chunks retrieval.
## 🌟 Why Private-AI?

Privacy is the key motivator! Private-AI addresses concerns in data-sensitive domains like healthcare and legal, ensuring your data stays under your control.

# 🤖 installation 

---

**Private-Ai Installation Guide**

### Base Requirements:
- Git clone Private-Ai repository:
  ```bash
  git clone https://github.com/AryanVBW/Private-Ai
  cd Private-Ai
  ```
- Install Python 3.11 (or 3.12)
- uding apt(linux)
  ```bash
  ```
- using pyenv:
  ```bash
  pyenv install 3.11
  pyenv local 3.11
  ```

- Install Poetry for dependency management.
```bash
  pip3 install poetry
  ```
### Dependencies Installation:
- Install make (OSX: `brew install make`, Windows: `choco install make`).
- Install dependencies:
  ```bash
  poetry install --with ui
  ```
### Local LLM Setup:
- Install extra dependencies for local execution:
  ```bash
  poetry install --with local
  ```
- Use the setup script to download embedding and LLM models:
  ```bash
  poetry run python scripts/setup
  ```
  
### Verification:
- Run `make run` or `poetry run python -m private_gpt`.
- Open http://localhost:8001 to see Gradio UI with a mock LLM echoing input.
# 👍👍👍All Done 👍👍👍

# For GPU utilization and customization, follow the steps below:

### Customization:
- Customize low-level parameters in `private_gpt/components/llm/llm_component.py`.
- Configure LLM options in `settings.yaml`.

### GPU Support:
- **OSX**: Build llama.cpp with Metal support.
  ```bash
  CMAKE_ARGS="-DLLAMA_METAL=on" pip install --force-reinstall --no-cache-dir llama-cpp-python
  ```

- **Windows NVIDIA GPU**: Install VS2022, CUDA toolkit, and run:
  ```powershell
  $env:CMAKE_ARGS='-DLLAMA_CUBLAS=on'; poetry run pip install --force-reinstall --no-cache-dir llama-cpp-python
  ```

- **Linux NVIDIA GPU and Windows-WSL**: Install CUDA toolkit and run:
  ```bash
  CMAKE_ARGS='-DLLAMA_CUBLAS=on' poetry run pip install --force-reinstall --no-cache-dir llama-cpp-python
  ```

### Troubleshooting:
- Check GPU support and dependencies for your platform.
- For C++ compiler issues, follow troubleshooting steps.

**Note**: If any issues, retry in verbose mode with `-vvv` during installations.

**Troubleshooting C++ Compiler**:
- **Windows 10/11**: Install Visual Studio 2022 and MinGW.
- **OSX**: Ensure Xcode is installed or install clang/gcc with Homebrew.

---


## 🧩 Architecture Highlights:

- **FastAPI-Based API:** Follows the OpenAI API standard, making it easy to integrate.
  
- **LlamaIndex Integration:** Leverages LlamaIndex for the RAG pipeline, providing flexibility and extensibility.




- **Present and Future:** Evolving into a gateway for generative AI models and primitives. Stay tuned for exciting new features!

## 💡 How to Contribute?

Contributions are welcome! Check the ProjectBoard for ideas. Ensure code quality with format and typing checks (run `make check`).

## 🤗Supporters:

Supported by Qdrant, Fern, and LlamaIndex. Influenced by projects like LangChain, GPT4All, LlamaCpp, Chroma, and SentenceTransformers.

👏 Thank you for contributing to the future of private and powerful AI with Private-AI!
📝 **License:** Apache-2.0
# Copyright Notice
This is a modified version of [PrivateGPT](https://github.com/imartinez/privateGPT). All rights and licenses belong to the PrivateGPT team.

© 2023 PrivateGPT Developers. All rights reserved.

