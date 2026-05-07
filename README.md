# 🛡️ Desafio de CI/CD: O Elo Perdido no Supply Chain

Bem-vindo ao desafio de segurança em ambientes de Integração e Entrega Contínua (CI/CD) da **Sec4US**. 

Neste cenário, você assume o papel de um pesquisador de segurança identificando falhas na infraestrutura da "Sec4US Cloud", uma empresa que utiliza **GitHub Actions** para automatizar o build e o teste de seus módulos internos que rodam em infraestrutura híbrida.

## 🏢 O Cenário
A empresa utiliza um servidor **Windows Server 2022** interno como um *Self-hosted Runner*. Por "medo" de ataques vindo da internet, eles implementaram um pipeline de duas etapas:

1.  **Build Pipeline:** O código de contribuidores externos é compilado em um ambiente Linux isolado do próprio GitHub.
2.  **Execution Pipeline:** Somente o artefato final (o módulo Python compilado) é baixado para o servidor Windows interno, onde é instalado e executado para validação em ambiente real.

O administrador do sistema garante que o ambiente é seguro pois:
*   O script principal (`main.py`) é imutável e reside permanentemente no Windows.
*   Toda execução ocorre dentro de um `venv` (ambiente virtual) que é destruído em seguida.
*   Nenhum segredo (Secrets) do GitHub é compartilhado com o Pull Request original.

## 🎯 Seu Objetivo
O objetivo é obter a **Flag de Administrador**. ?
Sabemos que a flag reside em algum lugar do drive `C:\` do servidor Windows, em um diretório que o administrador costuma usar para armazenar chaves e configurações críticas.

Você precisará de **dois passos**:
1.  **Enumeração:** Descobrir onde o arquivo de segredos está escondido.
2.  **Exfiltração:** Ler o conteúdo e enviá-lo para fora.

## 🔍 Informações Técnicas
*   O software corporativo no servidor utiliza um módulo chamado `not_exploitable`.
*   O script fixo no servidor possui a seguinte lógica:
    ```python
    import not_exploitable.core as core
    # ... inicialização do sistema ...
    core.run()
    ```
*   O pipeline de CI está dividido em:
    1.  **1 - Public Build:** Gera o pacote `.whl` do seu PR.
    2.  **2 - Internal Execution:** Instala o seu pacote no Windows e roda o software da empresa.

## 🛠️ Instruções para o Desafio
1.  **Enumeração (Obrigatório):** Você não sabe o caminho do arquivo. Use o seu primeiro Pull Request para injetar um código que liste diretórios (ex: `C:\`, `C:\Users\`, etc.) e envie essa lista para o seu servidor.
2.  **Exploit:** Após descobrir onde o "tesouro" está, atualize seu código para ler o arquivo e exfiltrá-lo.
3.  **Payload:** Utilize a biblioteca `requests` para enviar os dados para um listener sob seu controle (como o [Webhook.site](https://webhook.site)).
4.  **Atenção:** O arquivo `main.py` no servidor chama `core.run()`. Certifique-se de que sua lógica de ataque esteja acessível por essa chamada ou pela importação do módulo.

## ⚠️ Dica de Pentester
Um runner Windows self-hosted muitas vezes roda com privilégios de `LocalSystem` ou de um usuário administrativo para poder instalar dependências. O que mais esse usuário pode ler enquanto o seu pacote Python está sendo instalado ou executado? O tempo é curto, pois o ambiente virtual é deletado ao fim do job.

---
*Boa sorte! Lembre-se: em uma cadeia de suprimentos, a confiança é o vetor de ataque mais eficiente.*
