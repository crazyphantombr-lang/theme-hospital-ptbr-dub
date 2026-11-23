# Instalação — Theme Hospital PT-BR Beta V7

Este guia explica como substituir o pacote de áudio original pelo arquivo V7 e como restaurar o original.

## Antes de começar

- Tenha uma cópia legítima de Theme Hospital para PC.
- Feche o jogo e o CorsixTH antes de alterar arquivos.
- **Faça backup do `SOUND-0.DAT` original. Não pule esta etapa.**
- A V7 foi preparada como referência para Windows 10 + CorsixTH v0.70.1 Windows x64. Outras versões ainda precisam de testes.

## 1. Baixe o arquivo V7

- [Abrir `SOUND-0_PTBR_V7.DAT` no GitHub](https://github.com/crazyphantombr-lang/theme-hospital-ptbr-dub/blob/main/releases/v7/SOUND-0_PTBR_V7.DAT)
- [Download direto do arquivo](https://raw.githubusercontent.com/crazyphantombr-lang/theme-hospital-ptbr-dub/main/releases/v7/SOUND-0_PTBR_V7.DAT)

## 2. Localize o arquivo original

Encontre a pasta de dados do Theme Hospital utilizada pelo CorsixTH. Dentro dela, localize `SOUND-0.DAT`.

No ambiente usado durante o desenvolvimento, a pasta era:

`D:\DosBOX\CorsixTH-v0.70.1-Windows-x64\ThemeHospital\`

Sua instalação pode estar em outro local. Use a pasta efetivamente configurada no CorsixTH.

## 3. Faça uma cópia de segurança

1. Feche o jogo e o CorsixTH.
2. Copie `SOUND-0.DAT` para uma pasta segura ou mantenha uma cópia na mesma pasta.
3. Dê à cópia um nome fácil de reconhecer, por exemplo `SOUND-0_original_backup.DAT`.
4. Confirme que o backup existe antes de continuar.

## 4. Instale a V7

1. Copie `SOUND-0_PTBR_V7.DAT` para a pasta onde está o arquivo original.
2. Renomeie o `SOUND-0.DAT` original para `SOUND-0_original_backup.DAT`, caso ainda não tenha feito isso.
3. Renomeie o arquivo baixado de `SOUND-0_PTBR_V7.DAT` para `SOUND-0.DAT`.
4. Confira se o nome final está exatamente como `SOUND-0.DAT` e se o Windows não acrescentou uma extensão extra, como `.DAT.DAT`.
5. Inicie o CorsixTH.

A V7 substitui apenas o pacote `SOUND-0.DAT`. Não altere `SOUND-1.DAT` a `SOUND-5.DAT`.

## 5. Restaure o áudio original

Se quiser desfazer a instalação ou encontrar algum problema:

1. Feche o jogo e o CorsixTH.
2. Renomeie ou remova o `SOUND-0.DAT` da V7.
3. Renomeie `SOUND-0_original_backup.DAT` de volta para `SOUND-0.DAT`.
4. Inicie o CorsixTH novamente.

Não apague o backup enquanto estiver usando a versão beta.

## O que está incluído na V7

A V7 contém 45 clips em português brasileiro: 265–270, 280–288, 291–300, 312–321 e 329–338. Os demais clips permanecem como estavam no pacote-base.

## Limitações conhecidas

- A dublagem é parcial; não contempla todos os anúncios do jogo.
- A voz sintetizada é publicada como está nesta beta.
- Ainda não há simulação de alto-falante/PA, chiado ou estática. Esses efeitos ficam planejados para versões futuras.
- A validação estrutural do arquivo não substitui testes completos dentro do jogo.
- A compatibilidade foi preparada com base no ambiente de referência informado acima.

## Ajuda

Se houver problemas, informe a versão do CorsixTH, o sistema operacional e, se possível, em que momento o problema ocorreu. Preserve o backup para poder restaurar o áudio original.
