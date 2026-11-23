# Theme Hospital — Tradução e Dublagem PT-BR

**Projeto independente de tradução e dublagem de Theme Hospital para português brasileiro.**

![Status](https://img.shields.io/badge/status-beta-orange) ![Idioma](https://img.shields.io/badge/idioma-Portugu%C3%AAs%20Brasileiro-green) ![Plataforma](https://img.shields.io/badge/plataforma-PC-blue)

## Sobre o projeto

Este projeto tem como objetivo tornar **Theme Hospital**, clássico jogo de gerenciamento hospitalar da Bullfrog Productions, mais acessível ao público brasileiro por meio da tradução e dublagem para português brasileiro.

O trabalho envolve a identificação e transcrição das falas originais, a tradução e adaptação dos textos, a síntese das vozes em português brasileiro e a reconstrução dos arquivos de áudio utilizados pelo jogo.

A proposta é preservar o humor, a personalidade e o estilo característico dos anúncios originais, adaptando as falas para que soem naturais em português brasileiro.

Este é um projeto independente, desenvolvido por fãs e ainda em fase beta. A versão V7 mantém a interpretação sintetizada atual, sem simulação de alto-falante, chiado ou estática de sistema de som público. Esses efeitos e o aprimoramento da interpretação ficam planejados para versões futuras; não são uma escolha artística definitiva.

---

## Download — versão beta V7

A versão V7 disponibiliza o arquivo de áudio completo `SOUND-0_PTBR_V7.DAT`, com 45 clips em português brasileiro incorporados.

- **[Baixar SOUND-0_PTBR_V7.DAT](releases/v7/SOUND-0_PTBR_V7.DAT)**
- [Abrir a página do arquivo no GitHub](https://github.com/crazyphantombr-lang/theme-hospital-ptbr-dub/blob/main/releases/v7/SOUND-0_PTBR_V7.DAT)
- [Download direto](https://raw.githubusercontent.com/crazyphantombr-lang/theme-hospital-ptbr-dub/main/releases/v7/SOUND-0_PTBR_V7.DAT)

Consulte o [guia de instalação](docs/instalacao.md) antes de substituir qualquer arquivo. **Faça uma cópia de segurança do `SOUND-0.DAT` original.**

A V7 substitui o pacote de áudio em inglês `SOUND-0.DAT`. Os outros pacotes de áudio do jogo não são alterados.

## Estado atual — versão beta

O projeto está em desenvolvimento. Esta versão documenta os procedimentos técnicos, as traduções e os primeiros áudios já incorporados.

### Trabalho realizado

- Levantamento dos pacotes de áudio originais do jogo.
- Identificação dos clips de áudio e seus respectivos metadados.
- Transcrição de falas em inglês.
- Tradução e adaptação dos textos para português brasileiro.
- Organização de um índice de clips, transcrições e traduções.
- Síntese de vozes em português brasileiro utilizando ElevenLabs.
- Preparação e processamento dos arquivos de áudio sintetizados.
- Reconstrução do arquivo `SOUND-0.DAT`, preservando sua estrutura original.
- Incorporação de um primeiro conjunto de 45 clips traduzidos.
- Ajustes de volume para aproximar o nível sonoro das novas falas ao das gravações originais.

### Catálogo de falas

O intervalo de clips **231 a 376** foi catalogado com transcrições em inglês e traduções propostas para português brasileiro. O catálogo inclui avisos de chegada de pacientes, solicitações de médicos e funcionários, alertas de epidemias e terremotos, avisos de demissões, acontecimentos especiais e mensagens humorísticas.

**Importante:** uma fala estar transcrita e traduzida não significa que já tenha sido sintetizada, processada ou incorporada ao jogo.

### Áudios já incorporados

A V7 contém **45 clips traduzidos**, com ajustes de volume:

- 265–270
- 280–288
- 291–300
- 312–321
- 329–338

A implementação ainda é parcial e não representa uma dublagem completa do jogo.

---

## Pacotes de áudio do jogo

| Arquivo | Idioma |
|---|---|
| `SOUND-0.DAT` | Inglês |
| `SOUND-1.DAT` | Francês |
| `SOUND-2.DAT` | Alemão |
| `SOUND-3.DAT` | Italiano |
| `SOUND-4.DAT` | Espanhol |
| `SOUND-5.DAT` | Sueco |

O pacote `SOUND-0.DAT` foi escolhido como base para o desenvolvimento da versão brasileira. Na instalação, a V7 deve ser usada no lugar desse arquivo, mantendo os demais pacotes intactos.

## Processo técnico de reconstrução do SOUND-0.DAT

O arquivo `SOUND-0.DAT` contém blocos de áudio e referências internas; por isso, a substituição exige cuidados com a estrutura binária e com a localização dos dados.

### 1. Análise da estrutura original

O arquivo de referência possui:

- Tamanho: **16.634.862 bytes**.
- Total identificado: **376 blocos RIFF/WAVE**.
- Formato das falas analisadas: PCM, mono, 22.050 Hz, 8 bits.

O índice registra número do clip, metadado, duração, tamanho e posição dentro do arquivo DAT.

### 2. Identificação dos clips

| Clip | Metadado | Conteúdo | Amostra (MP3) |
|---:|---|---|---|
| 265 | `reqd001.wav` | Solicitação para o Eletrocardiograma | [Ouvir](samples/mp3/clip-265.mp3) |
| 266 | `reqd002.wav` | Solicitação para a Sala do Scanner | [Ouvir](samples/mp3/clip-266.mp3) |
| 267 | `reqd003.wav` | Solicitação para a Psiquiatria | [Ouvir](samples/mp3/clip-267.mp3) |
| 268 | `reqd004.wav` | Solicitação para a Clínica de Fraturas | [Ouvir](samples/mp3/clip-268.mp3) |
| 269 | `reqd005.wav` | Solicitação para a Clínica de Linguarudos | [Ouvir](samples/mp3/clip-269.mp3) |
| 270 | `reqd014.wav` | Solicitação para o Inflador de Cabeças | [Ouvir](samples/mp3/clip-270.mp3) |

*As amostras MP3 são apenas demonstrativas. Não devem ser copiadas para a pasta do jogo nem substituem o arquivo DAT.*

### 3. Preparação e substituição dos áudios

As falas são sintetizadas em português brasileiro e processadas para o formato de referência PCM, mono, 22.050 Hz e 8 bits. A reconstrução procura preservar posições, offsets, cabeçalhos, estrutura, tamanho total e clips ainda não traduzidos.

### 4. Ajuste de volume e verificação

As novas falas passam por normalização individual, utilizando o nível RMS do áudio original correspondente como referência, e controle de pico. No pacote V7, o arquivo reconstruído manteve o tamanho de **16.634.862 bytes**, com os 376 blocos identificados. A verificação estrutural não substitui testes de reprodução dentro do jogo.

## Ferramentas e ambiente

- **Síntese:** ElevenLabs.
- **Processamento:** ferramentas de conversão, edição, normalização e controle de pico.
- **Ambiente:** Windows 10, Theme Hospital original para PC e CorsixTH v0.70.1 Windows x64.

A compatibilidade com outras versões ainda precisa ser verificada.

## Estrutura do repositório

```text
Theme-Hospital-PTBR/
├── README.md
├── docs/instalacao.md
├── translations/
├── samples/mp3/
└── releases/
    ├── README.md
    └── v7/
        ├── README.md
        └── SOUND-0_PTBR_V7.DAT
```

## Próximas etapas

- [ ] Revisar traduções e padronizar a terminologia.
- [ ] Completar a síntese das falas ainda não dubladas.
- [ ] Incorporar novos clips ao arquivo DAT.
- [ ] Testar os arquivos em diferentes situações e configurações.
- [x] Disponibilizar um arquivo DAT V7 pronto para instalação.
- [x] Documentar backup e restauração.
- [ ] Aprimorar interpretação e explorar efeitos de alto-falante/PA em versões futuras.

## Como contribuir

Contribuições são bem-vindas: revisão de traduções, sugestões de adaptação cultural e humor, identificação e transcrição de falas, revisão de pronúncia, processamento de áudio, testes de compatibilidade e documentação. Preserve o número original do clip e seu metadado.

## Aviso legal

Theme Hospital é propriedade de seus respectivos titulares. Este é um projeto independente, sem vínculo oficial, patrocínio ou aprovação da Bullfrog Productions, Electronic Arts ou CorsixTH. O usuário deve possuir uma cópia legítima do jogo. Os direitos sobre o jogo e seus arquivos originais permanecem com seus respectivos titulares.

## Créditos

- **Projeto:** Theme Hospital PT-BR.
- **Jogo original:** Theme Hospital — Bullfrog Productions.
- **Síntese de voz:** ElevenLabs.
- **Ambiente de execução:** CorsixTH.

**Versão:** Beta V7  
**Status:** Em desenvolvimento  
**Idioma-alvo:** Português brasileiro (PT-BR)
