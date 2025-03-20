import requests
from unittest.mock import Mock

# Mock da resposta da API, já que não se tem endpoint implementado e registros no banco de dados
def mock_obter_logs():
    
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {

            # Exemplo de entrada correta
            "id": 1,
            "action": "Marcou um novo atendimento",
            "action_time": "2024-03-23T13:57:00",
            "user_id": 123,
            "details": "Atendimento marcado para o aluno João Silva",
            "appointment_id": 456
        },
        {
            # Exemplo de entrada correta
            "id": 2,
            "action": "Editou um atendimento",
            "action_time": "2024-03-21T09:32:00",
            "user_id": 456,
            "details": "Atendimento editado para o aluno Maria Souza",
            "appointment_id": 789
            
           
        }
        
    ]
    return mock_response

# Função que simula a requisição GET para obter logs
def obter_logs():
    requests.get = mock_obter_logs()
    response = requests.get
    
    # Verifica o resultado
    if response.status_code == 200:
        logs = response.json()
        print("Test PASSED: Logs retornados com sucesso!")
        print("Quantidade de logs:", len(logs))
        print("Exemplo de log:", logs[0] if logs else "Nenhum log encontrado")
    else:
        print("Test FAILED: Falha ao obter logs.")
        print("Status code:", response.status_code)
        print("Mensagem de erro:", response.text)

# Executa o teste
obter_logs()