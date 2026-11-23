# Instalação — Beta V7

## Antes de começar

- Use uma cópia legítima de Theme Hospital para PC.
- Feche o jogo e o CorsixTH antes de substituir qualquer arquivo.
- Faça uma cópia de segurança do `SOUND-0.DAT` original. Não pule esta etapa.
- A V7 foi preparada para o `SOUND-0.DAT` de referência com 16.634.862 bytes e SHA-256:
  `ed93e9310fd83a7e71837c50f22c63c05605c118ffd84e74b91c4a928bd8c051`.

## 1. Localize e faça backup

Na instalação usada durante o desenvolvimento, a pasta do jogo era:

`D:\DosBOX\CorsixTH-v0.70.1-Windows-x64\ThemeHospital\`

Sua instalação pode estar em outro local. Localize nela o arquivo `SOUND-0.DAT`.

1. Feche o jogo.
2. Copie `SOUND-0.DAT` para uma pasta segura.
3. Renomeie a cópia para `SOUND-0_original_backup.DAT`.
4. Confirme que o backup existe e não está vazio.

## 2. Gere o arquivo PT-BR

Extraia a pasta `patch` deste pacote. Abra o Prompt de Comando nessa pasta e execute:

```bat
python apply_patch.py "C:\caminho\para\ThemeHospital\SOUND-0.DAT"
```

O aplicador verifica o tamanho e o SHA-256 do arquivo original e cria `SOUND-0_PTBR_V7.DAT` na pasta atual. Ele não altera o original. Se a verificação falhar, não tente forçar a aplicação: sua versão do arquivo-base é diferente da referência da beta.

## 3. Substitua o arquivo

1. Confirme que `SOUND-0_PTBR_V7.DAT` foi criado e tem 16.634.862 bytes.
2. Copie esse arquivo para a pasta do jogo.
3. Renomeie o arquivo gerado para `SOUND-0.DAT` (se necessário, primeiro guarde o original em backup fora da pasta).
4. Inicie o CorsixTH e teste o jogo normalmente.

## 4. Como restaurar o original

Se houver qualquer problema:

1. Feche o jogo e o CorsixTH.
2. Remova ou renomeie o `SOUND-0.DAT` modificado.
3. Copie `SOUND-0_original_backup.DAT` de volta para a pasta do jogo.
4. Renomeie-o para `SOUND-0.DAT`.

Assim, a instalação retorna ao áudio original.

## Observações

- A V7 contém 45 clips em português brasileiro; não é uma dublagem completa.
- As amostras MP3 do repositório são apenas para demonstração e não são arquivos de jogo.
- A validação estrutural do DAT não substitui testes de reprodução no jogo.
- A V7 mantém a voz sintetizada atual. Efeitos de alto-falante, chiado/estática e refinamento de interpretação ficam para versões futuras.
