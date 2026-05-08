import os
import sys

# Garante que o venv consiga importar o módulo instalado
try:
    import not_exploitable.core as core
except ImportError:
    print("Erro: Módulo not_exploitable não encontrado.")
    sys.exit(1)

print(f"--- Sistema de Gestão Interna Sec4US ---")
print(f"Executando como usuário: {os.getlogin()}")
print(f"Iniciando rotina de processamento...")

# Chama a função do módulo principal
core.run()

print("Processamento finalizado.")
