import requests

def check_domain_availability(domain):
    url = f"https://api.namecheap.com/xml.response?ApiUser=YOUR_API_USER&ApiKey=YOUR_API_KEY&UserName=YOUR_USERNAME&Command=namecheap.domains.check&DomainList={domain}&ClientIp=127.0.0.1"
    response = requests.get(url)
    if response.status_code == 200:
        xml_data = response.text
        # Aqui você pode analisar o XML para verificar a disponibilidade do domínio
        # Por simplicidade, vamos assumir que se a resposta contiver "Available", o domínio está disponível
        if "Available" in xml_data:
            return True
    return False

def main():
    domains = input("Digite os domínios separados por vírgula: ").split(',')
    for domain in domains:
        domain = domain.strip()
        if check_domain_availability(domain):
            print(f"{domain} está disponível para compra.")
        else:
            print(f"{domain} não está disponível.")

if __name__ == '__main__':
    main()
