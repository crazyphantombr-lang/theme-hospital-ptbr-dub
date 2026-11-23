# Theme Hospital — Tradução e Dublagem PT-BR

**Projeto independente de tradução e dublagem de Theme Hospital para português brasileiro.**

![Status](https://img.shields.io/badge/status-beta-orange)
![Idioma](https://img.shields.io/badge/idioma-Portugu%C3%AAs%20Brasileiro-green)
![Plataforma](https://img.shields.io/badge/plataforma-PC-blue)

## Sobre o projeto

Este projeto tem como objetivo tornar **Theme Hospital**, clássico jogo de gerenciamento hospitalar da Bullfrog Productions, mais acessível ao público brasileiro por meio da tradução e dublagem para português brasileiro.

O trabalho envolve a identificação e transcrição das falas originais, a tradução e adaptação dos textos, a síntese das vozes em português brasileiro e a reconstrução dos arquivos de áudio utilizados pelo jogo.

A proposta é preservar o humor, a personalidade e o estilo característico dos anúncios originais, adaptando as falas para que soem naturais em português brasileiro.

Este é um projeto independente, desenvolvido por fãs e ainda em fase beta. A versão V7 mantém a interpretação sintetizada atual, sem simulação de alto-falante, chiado ou estática de sistema de som público. Esses efeitos e o aprimoramento da interpretação ficam planejados para versões futuras; não são uma escolha artística definitiva.

---

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

O intervalo de clips **231 a 376** foi catalogado com transcrições em inglês e traduções propostas para português brasileiro.

O catálogo inclui:

- Avisos de chegada de pacientes.
- Solicitações de médicos, enfermeiros e funcionários.
- Alertas de epidemias e terremotos.
- Avisos de demissões e acontecimentos especiais.
- Mensagens aleatórias e anúncios do hospital.
- Mensagens humorísticas características do jogo.

**Importante:** uma fala estar transcrita e traduzida não significa que já tenha sido sintetizada, processada ou incorporada ao jogo.

### Áudios já incorporados

O pacote de trabalho V7 contém um primeiro conjunto de **45 clips traduzidos**, com ajustes de volume.

Os clips incorporados são:

- 265–270
- 280–288
- 291–300
- 312–321
- 329–338

A implementação ainda é parcial e não representa uma dublagem completa do jogo.

---

## Pacotes de áudio do jogo

Durante a análise dos arquivos originais, identificamos seis pacotes de áudio:

| Arquivo | Idioma |
|---|---|
| `SOUND-0.DAT` | Inglês |
| `SOUND-1.DAT` | Francês |
| `SOUND-2.DAT` | Alemão |
| `SOUND-3.DAT` | Italiano |
| `SOUND-4.DAT` | Espanhol |
| `SOUND-5.DAT` | Sueco |

O pacote `SOUND-0.DAT` foi escolhido como base para o desenvolvimento da versão brasileira.

Os demais pacotes podem servir como referências comparativas para a análise da organização dos áudios e das diferenças entre as versões linguísticas.

Eles não são tratados como versões em português brasileiro.

---

## Processo técnico de reconstrução do SOUND-0.DAT

Uma das partes centrais do projeto é a substituição dos áudios originais sem comprometer a estrutura do arquivo de som utilizado pelo jogo.

O arquivo `SOUND-0.DAT` não é simplesmente uma pasta compactada de arquivos WAV. Por isso, a substituição exige cuidados com a estrutura binária e com a localização dos dados de áudio.

### 1. Análise da estrutura original

O arquivo original utilizado como referência possui:

- Tamanho: **16.634.862 bytes**.
- Total identificado: **376 blocos de áudio RIFF/WAVE**.
- Formato de áudio das falas analisadas: PCM.
- Canais: mono.
- Taxa de amostragem: 22.050 Hz.
- Profundidade: 8 bits.

Cada bloco de áudio possui cabeçalho e dados de áudio. O índice do projeto registra informações como número do clip, metadado, duração, tamanho e posição dentro do arquivo DAT.

### 2. Identificação dos clips

Os clips são identificados por seus números e pelos nomes de metadados originais.

Exemplos:

| Clip | Metadado | Conteúdo | Amostra (MP3) |
|---:|---|---|---|
| 265 | `reqd001.wav` | Solicitação para o Eletrocardiograma | [Ouvir](samples/mp3/clip-265.mp3) |
| 266 | `reqd002.wav` | Solicitação para a Sala do Scanner | [Ouvir](samples/mp3/clip-266.mp3) |
| 267 | `reqd003.wav` | Solicitação para a Psiquiatria | [Ouvir](samples/mp3/clip-267.mp3) |
| 268 | `reqd004.wav` | Solicitação para a Clínica de Fraturas | [Ouvir](samples/mp3/clip-268.mp3) |
| 269 | `reqd005.wav` | Solicitação para a Clínica de Linguarudos | [Ouvir](samples/mp3/clip-269.mp3) |
| 270 | `reqd014.wav` | Solicitação para o Inflador de Cabeças | [Ouvir](samples/mp3/clip-270.mp3) |

*As amostras MP3 são apenas demonstrativas. Não devem ser copiadas para a pasta do jogo nem substituem os arquivos de áudio usados pelo jogo.*

A correspondência entre o número do clip e o metadado é essencial para evitar que uma fala seja reproduzida no contexto errado.

### 3. Preparação dos novos áudios

As falas traduzidas são sintetizadas em português brasileiro e processadas para atender às características técnicas dos arquivos originais.

O formato de referência utilizado é:

- PCM.
- Mono.
- 22.050 Hz.
- 8 bits.

Também são realizados ajustes de duração e volume para adequar os novos áudios aos espaços disponíveis.

### 4. Substituição dos dados de áudio

A reconstrução é feita diretamente sobre uma cópia do arquivo DAT original.

O procedimento procura preservar:

- A posição original dos blocos de áudio.
- Os offsets registrados no arquivo.
- Os cabeçalhos e a estrutura dos blocos.
- O tamanho total do arquivo.
- Os clips que ainda não foram traduzidos.

Quando um novo áudio ocupa menos espaço que o original, o espaço restante é preenchido para preservar o tamanho reservado ao bloco.

Dessa forma, evita-se deslocar os blocos seguintes e comprometer as referências internas do arquivo.

### 5. Ajuste de volume

As novas falas passam por normalização individual, utilizando o nível RMS do áudio original correspondente como referência.

Também é aplicado controle de pico para evitar distorções e valores excessivos.

O objetivo é reduzir diferenças perceptíveis de volume entre as falas originais e as sintetizadas.

### 6. Verificação do arquivo reconstruído

Após a substituição, são realizadas verificações estruturais, incluindo:

- Comparação do tamanho do arquivo antes e depois.
- Verificação da quantidade de blocos identificados.
- Conferência dos clips substituídos.
- Preservação dos dados dos clips não modificados.
- Verificação dos parâmetros de áudio.

No pacote V7, o arquivo reconstruído manteve o tamanho original de **16.634.862 bytes**, com os 376 blocos de áudio identificados.

Essas verificações são estruturais e não substituem os testes de reprodução dentro do jogo.

---

## Ferramentas utilizadas

### ElevenLabs

Utilizado para sintetizar as falas em português brasileiro a partir dos textos traduzidos.

A síntese de voz permite produzir os novos áudios sem a necessidade de gravar individualmente todas as falas com atores humanos.

As falas são preparadas considerando o estilo dos anúncios originais, buscando preservar clareza, ritmo e personalidade.

### Ferramentas de processamento de áudio

Utilizadas para:

- Conversão para o formato exigido pelo jogo.
- Ajustes de duração.
- Normalização de volume.
- Controle de pico.
- Preparação dos arquivos WAV para incorporação ao DAT.

### CorsixTH

O CorsixTH é utilizado como ambiente de execução para verificar o funcionamento do jogo com os arquivos modificados.

Versão utilizada durante o desenvolvimento:

`CorsixTH v0.70.1 — Windows x64`

---

## Ambiente de desenvolvimento

Ambiente utilizado como referência:

| Componente | Versão ou configuração |
|---|---|
| Sistema operacional | Windows 10 |
| Jogo | Theme Hospital original para PC |
| Ferramenta | CorsixTH v0.70.1 |
| Arquitetura | Windows x64 |
| Pacote de áudio de referência | SOUND-0 (inglês) |
| Idioma do projeto | Português brasileiro |

A compatibilidade com outras versões do jogo, sistemas operacionais e versões do CorsixTH ainda precisa ser verificada.

---

## Estrutura do repositório

```text
Theme-Hospital-PTBR/
├── README.md
├── docs/
│   ├── instalacao.md
│   ├── RELATORIO_V7_VOLUME_PTBR.txt
│   └── Auditoria_Volume_PTBR_V7.csv
├── translations/
│   └── Indice_Audios_Theme_Hospital_0-5_com_traducao_V7.csv
├── samples/
│   └── mp3/                 # seis amostras demonstrativas
├── releases/
│   └── v7/                  # pacote de patch e notas da versão
└── tools/
    └── apply_patch.py       # aplicador incluído no pacote V7
```

A estrutura poderá ser ampliada conforme o projeto evoluir.

---

## Próximas etapas

- [ ] Revisar as traduções e padronizar a terminologia.
- [ ] Completar a síntese das falas ainda não dubladas.
- [ ] Processar os novos áudios para o formato original.
- [ ] Incorporar novos clips ao arquivo DAT.
- [ ] Verificar a correspondência entre cada clip e sua fala no jogo.
- [ ] Testar os arquivos em diferentes situações de jogo.
- [x] Preparar um método de instalação e restauração dos arquivos originais.
- [ ] Documentar o processo de reconstrução do arquivo DAT.
- [ ] Ampliar a compatibilidade com diferentes versões.
- [ ] Publicar novas versões beta e, futuramente, uma versão estável.

---

## Como contribuir

Contribuições são bem-vindas!

Você pode ajudar com:

- Revisão de traduções.
- Sugestões de adaptação cultural e humor.
- Identificação e transcrição de falas.
- Revisão de pronúncia e interpretação das vozes sintetizadas.
- Processamento e edição de áudio.
- Testes de compatibilidade.
- Documentação e ferramentas.

Ao contribuir, procure preservar o número original do clip e seu metadado. Isso ajuda a evitar que uma fala seja associada ao áudio errado.

---

## Aviso legal

Theme Hospital é propriedade de seus respectivos titulares de direitos autorais.

Este é um projeto independente, sem vínculo oficial, patrocínio ou aprovação da Bullfrog Productions, Electronic Arts ou CorsixTH.

O projeto é desenvolvido por fãs, com o objetivo de produzir uma tradução e dublagem não oficial para português brasileiro.

**Não distribuímos o jogo original nem seus arquivos proprietários.**

O usuário deve possuir uma cópia legítima do jogo. O repositório deve priorizar documentação, traduções, índices, ferramentas e patches que possam ser aplicados a uma cópia original, respeitando os direitos dos titulares.

---

## Créditos

- **Projeto:** Theme Hospital PT-BR.
- **Jogo original:** Theme Hospital — Bullfrog Productions.
- **Síntese de voz:** ElevenLabs (voz da V7 sem efeitos de alto-falante/PA; aprimoramentos planejados para versões futuras).
- **Ambiente de execução:** CorsixTH.
- **Comunidade:** colaboradores de tradução, transcrição, síntese, edição de áudio, programação e testes.

---

**Versão:** Beta  
**Status:** Em desenvolvimento  
**Idioma-alvo:** Português brasileiro (PT-BR)

*Este README será atualizado conforme novas etapas da tradução e dublagem forem concluídas.*