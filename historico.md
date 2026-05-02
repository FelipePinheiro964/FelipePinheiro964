# Histórico de Alterações

## Versão 1.0 - Adição do Script Python para Verificar Disponibilidade de Domínios

- **Data**: [Insira a Data]
- **Descrição**: Adicionado script Python (`domain_checker.py`) para verificar a disponibilidade de domínios usando a API Namecheap.
- **Responsável**: [Seu Nome]

### Detalhes do Script

O script `domain_checker.py` realiza as seguintes funcionalidades:

1. **Função `check_domain_availability(domain)`**:
   - Envia uma solicitação à API Namecheap para verificar a disponibilidade de um domínio.
   - Retorna `True` se o domínio estiver disponível, caso contrário, retorna `False`.

2. **Função `main()`**:
   - Solicita ao usuário que insira uma lista de domínios separados por vírgula.
   - Verifica a disponibilidade de cada domínio usando a função `check_domain_availability`.
   - Imprime o resultado para cada domínio.

### Como Usar

1. Salve o código acima em um arquivo chamado `domain_checker.py`.
2. Execute o script:
   ```sh
   python domain_checker.py
   ```
3. Insira uma lista de domínios quando solicitado, separados por vírgula.

Este é um exemplo básico e pode ser expandido com mais funcionalidades como verificação de múltiplas APIs, tratamento de erros, etc.
