# speak_api_integracao
API criada para integrar recurso de transcrição de voz em texto

## Para instalar:
Foi necessário instalar o "pyenv" gerenciador de versões do Python:
### Usando pip (existente para python instalado)
Powershell or Git Bash: 
pip install pyenv-win --target $HOME\\.pyenv

cmd.exe: 
pip install pyenv-win --target %USERPROFILE%\.pyenv

Após instalado, digitar o comando: 

pyenv install -l (definir qual versão do python a ser instalada)

pyenv install 2.7.18-win32

## Para isolar o ambiente e setar o interpretador python dentro desta versão escolhida

pip install vitualenv

virtualenv -p (caminho da versão do python escolhida dentro do pyenv) <nome_do_ambiente_virtual>

## Ativando o ambiente virtual

<nome_do_ambiente_virtual>\Scripts\activate

### Atentar que às vezes a "política de privacidade" para rodar Scripts como este acima, estão "restritas"

No PowerShell, como administrador, digite o comando: 

set-executionpolicy unrestricted

## Clonar o projeto do [GitHub] (https://github.com/GetulioCastro/transcreve_voz)

Digitar o comando: pip install -r requirements.txt

## Aí é sóo brincar de transcrição de voz

## Também é possível aumentar ou diminuir o tempo de "espera" nas pausas de voz 

