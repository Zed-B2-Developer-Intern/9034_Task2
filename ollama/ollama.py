import requests

def ask_ollama(prompt, model="llama3.2:1b"):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()["response"]
    except requests.exceptions.RequestException as e:
        return f"Error communicating with Ollama: {e}"

def main():
    print("💬 Ollama Chat (LLaMA 3.2:1B)")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        reply = ask_ollama(user_input)
        print("Ollama:", reply)
        print()

if __name__ == "__main__":
    main()
