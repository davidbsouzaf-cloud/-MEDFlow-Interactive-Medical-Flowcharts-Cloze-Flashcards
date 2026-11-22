# MEDFlow – Criador de Fluxogramas Médicos Interativos e Flashcards Cloze

**Transforme conceitos médicos complexos em experiências visuais de aprendizagem.**

O MEDFlow é um complemento (add-on) para o Anki que permite criar fluxogramas médicos interativos e transformá-los em flashcards Cloze (preenchimento de lacunas). Ele combina organização visual, raciocínio clínico e o sistema de repetição espaçada do Anki para tornar o estudo mais ativo e dinâmico.

Inspirado no projeto **ZeestMedical**, o MEDFlow foi desenvolvido de forma independente para oferecer um editor de fluxogramas integrado ao Anki.

## ✦ PRINCIPAIS FUNCIONALIDADES

### 1. 🎨 Editor de Fluxogramas Interativo

Construa algoritmos médicos utilizando três tipos de elementos:

- **Etapa / Caixa (Step / Box):** representa uma etapa, procedimento, achado clínico ou informação.
- **Decisão (Decision):** representa uma decisão clínica ou ponto de ramificação, com formato de losango.
- **Informação (Information):** destaca explicações adicionais ou detalhes importantes.

Movimente, redimensione e organize os elementos livremente para criar caminhos clínicos complexos.

- Guias automáticas de alinhamento.
- Personalização das cores, bordas e aparência das caixas.
- Seleção múltipla e edição simultânea de elementos.
- Alteração do tipo de várias caixas selecionadas ao mesmo tempo.
- Funções de desfazer e refazer alterações.

**Atalhos inspirados no XMind:** o MEDFlow utiliza os mesmos atalhos de teclado do XMind para a criação de diferentes tipos de caixas, tornando a construção dos fluxogramas mais rápida e intuitiva.

### 2. 🔗 Conexões e Fluxos Clínicos

- Conecte elementos utilizando pontos azuis de conexão que podem ser arrastados.
- Crie relações entre elementos principais e secundários.
- Reconecte setas arrastando suas extremidades.
- Adicione rótulos às setas, como "Sim", "Não", "Positivo", "Negativo" ou critérios clínicos.
- Organize árvores de decisão diagnóstica e terapêutica.

### 3. 🖼️ Image Nodes – Imagens Diretamente no Fluxograma

Insira imagens diretamente no fluxograma como elementos visuais independentes.

Diferentemente das imagens adicionadas ao conteúdo complementar (Extra), os Image Nodes passam a fazer parte da própria estrutura do fluxograma.

- Insira imagens diretamente na área de edição.
- Cole imagens copiadas para o editor.
- Redimensione e posicione as imagens livremente.
- Conecte imagens a outras caixas utilizando setas.
- Adicione legendas às imagens.
- Exiba as imagens diretamente nos cartões gerados pelo Anki.
- As legendas também são ocultadas quando a imagem correspondente é escondida pelo Cloze.

Ideal para anatomia, histologia, radiologia, patologia, dermatologia e outros conteúdos médicos que dependem de imagens.

### 4. 🃏 Geração de Flashcards Cloze

Atribua números Cloze individualmente aos elementos do fluxograma. Elementos que compartilham o mesmo número pertencem ao mesmo cartão do Anki, enquanto números diferentes geram cartões separados.

**Funcionalidades:**

- Atribua números Cloze específicos ou incremente automaticamente a numeração.
- Visualize o fluxograma completo no cartão.
- Identifique o elemento que está sendo testado por meio de destaque visual.
- Revele o elemento oculto ao clicar nele.
- Revise o fluxograma completo ou utilize o Focus Flow para estudar ramificações específicas.

**Exemplo:** Elemento 1 → c1 | Elemento 2 → c2 | Elemento 3 → c3

Clique em **Salvar e Gerar Cartões (Save and Generate Cards)** para sincronizar seu fluxograma com o Anki.

### 5. 🎯 Focus Flow – Revisão Progressiva por Ramificações

O Focus Flow introduz uma nova maneira de revisar fluxogramas complexos, permitindo percorrer ramificações selecionadas progressivamente.

Em vez de exibir todo o algoritmo de uma só vez, você pode definir um caminho específico e revisar seus elementos etapa por etapa.

**Como funciona:**

- Selecione as caixas pertencentes a uma ramificação utilizando Shift + Clique ou Shift + Arraste.
- Como alternativa, selecione apenas a primeira caixa para incluir automaticamente os elementos conectados abaixo dela.
- Ative o Focus pelo botão de alvo ou pelo atalho `Ctrl + Shift + F`.
- Os elementos selecionados recebem uma identificação visual de Focus.
- Durante a revisão, os cartões acompanham progressivamente o caminho selecionado, apresentando um Cloze por vez.

**Durante a revisão:**

- A ramificação começa pelo seu elemento inicial.
- Apenas o caminho relevante é apresentado.
- As setas orientam a progressão para a próxima etapa.
- Ramificações não relacionadas ficam ocultas.
- Elementos sem Cloze permanecem visíveis junto aos elementos relacionados.
- Cartões sem configurações de Focus continuam exibindo o fluxograma completo.

Também é possível alternar entre a ramificação selecionada e o fluxograma completo utilizando os controles de olho e alvo.

### 6. 📱 Melhorias na Revisão em Dispositivos Móveis

O MEDFlow recebeu melhorias para tornar os cartões mais legíveis em telas menores, incluindo o AnkiMobile.

- Adaptação automática do fluxograma ao tamanho da tela.
- Priorização do elemento Cloze ativo, evitando reduzir excessivamente todo o diagrama.
- Centralização do elemento relevante em um nível de zoom mais legível.
- Possibilidade de enquadrar o fluxograma completo quando necessário.
- Adaptação a alterações no tamanho e na orientação da tela.
- Controles de revisão adaptados à interação por toque.

O objetivo é manter algoritmos médicos complexos legíveis e funcionais durante a revisão pelo celular.

### 7. 💡 Dicas nas Caixas (Box Hints)

Adicione dicas individuais aos elementos do fluxograma sem revelar diretamente suas respostas.

- Adicione uma dica utilizando a ferramenta correspondente.
- As dicas aparecem em verde acima da caixa no editor.
- Durante a revisão, um botão **+** aparece quando a caixa correspondente está oculta pelo Cloze.
- Clique no botão para revelar a dica no lugar do conteúdo oculto.
- Clique novamente para ocultá-la.

Ideal para pistas, lembretes e informações que auxiliam na recuperação ativa do conteúdo.

### 8. 📝 Conteúdo Complementar (Extra)

Anexe explicações e imagens complementares a elementos individuais.

- Adicione explicações clínicas e anotações detalhadas.
- Inclua observações, informações importantes e detalhes adicionais.
- Anexe imagens ao conteúdo complementar.
- Exiba o conteúdo correspondente durante a revisão do cartão.

O conteúdo Extra aparece no verso do cartão Cloze correspondente.

### 9. 📚 Templates – Modelos Prontos de Fluxogramas

Economize tempo começando com estruturas de fluxogramas prontas, em vez de construir todos os diagramas do zero.

- Utilize modelos predefinidos para assuntos médicos e algoritmos clínicos.
- Salve seus próprios modelos personalizados.
- Salve apenas as caixas selecionadas ou o fluxograma inteiro como modelo.
- Reutilize modelos em outras notas.
- Restaure os modelos originais quando necessário.
- Os modelos personalizados são armazenados separadamente dos arquivos do editor, ajudando a preservá-los durante atualizações do add-on.

### 10. ↩️ Desfazer e Refazer (Undo/Redo)

Edite com mais segurança utilizando o histórico de ações do editor.

- `Ctrl + Z` – Desfazer.
- `Ctrl + Y` ou `Ctrl + Shift + Z` – Refazer.
- Recupere disposições anteriores de caixas e setas.
- Mantenha até 200 estados de edição no histórico.

### 11. ✍️ Formatação de Texto e Personalização Visual

Personalize o conteúdo e a aparência dos elementos para melhorar a organização e a legibilidade.

- Negrito, itálico e sublinhado.
- Diferentes tamanhos e famílias de fontes.
- Listas com marcadores e numeração.
- Cores e bordas personalizáveis para as caixas.
- Diferentes estilos e cores de setas.
- Formatação individual de elementos e conexões.
- Opções para limpar a formatação.

### 12. 📤 Importação e Exportação

- Exporte fluxogramas em arquivos JSON.
- Importe diagramas exportados anteriormente.
- Faça cópias de segurança, reutilize e modifique algoritmos existentes.
- Compartilhe estruturas de fluxogramas com outros usuários.

### 13. 🧭 Navegação e Área de Trabalho

- Aumente e diminua o zoom ou enquadre todo o fluxograma na área de trabalho.
- Movimente-se pelo painel arrastando o fundo.
- Aplique zoom ao redor do cursor utilizando Ctrl + Roda do Mouse.
- Alinhe elementos automaticamente com guias visuais.
- Selecione vários elementos utilizando Shift + Clique ou Shift + Arraste.
- Recolha a barra lateral para obter uma área de trabalho mais limpa.
- Compatibilidade com o modo escuro do Anki.
- Preserva o nível de zoom e a posição do painel entre a frente e o verso dos cartões e entre cartões durante a mesma sessão de revisão.

### 14. 🔒 Privacidade e Armazenamento

- Nenhum dado é enviado para servidores externos; tudo é armazenado localmente no seu computador.
- Os fluxogramas são salvos em formato JSON diretamente na nota do Anki, facilitando backups, exportações e compartilhamento de baralhos.
- As imagens são armazenadas na pasta de mídia do Anki e referenciadas automaticamente, permitindo sua inclusão em exportações e baralhos compartilhados.

## ✦ COMO UTILIZAR O MEDFLOW

### Passo 1 – Instalar e Abrir o Editor

Instale o add-on e reinicie o Anki. O tipo de nota **MedFlow** é criado automaticamente. Crie uma nova nota utilizando esse tipo e clique no botão **Alg** para abrir o editor.

### Passo 2 – Construir o Fluxograma

Adicione elementos do tipo Etapa, Decisão e Informação. Utilize os atalhos de teclado para criar caixas rapidamente. Dê dois cliques em um elemento para editar seu texto.

### Passo 3 – Conectar os Elementos

Arraste um ponto azul de conexão de um elemento para outro para criar uma seta. Como alternativa, utilize o **Link Mode** para selecionar um elemento principal e, em seguida, seus elementos secundários.

### Passo 4 – Atribuir Números Cloze

Selecione um elemento e insira um número no campo CLOZE. Clique em **Apply** para atribuí-lo ou em **+1** para incrementar e aplicar o próximo número.

### Passo 5 – Adicionar Imagens e Conteúdo Extra

Insira imagens diretamente no fluxograma utilizando Image Nodes ou selecione um elemento e abra a ferramenta **Extra** para adicionar anotações e imagens complementares.

### Passo 6 – Organizar e Personalizar

Utilize a seleção múltipla, altere os tipos das caixas, personalize as cores, adicione dicas e organize seu fluxograma. Você também pode salvar estruturas frequentemente utilizadas como modelos.

### Passo 7 – Configurar o Focus Flow (Opcional)

Selecione uma ramificação utilizando Shift + Clique ou Shift + Arraste. Em seguida, ative o Focus pelo botão de alvo ou pelo atalho `Ctrl + Shift + F`.

### Passo 8 – Salvar e Gerar Cartões

Utilize os botões abaixo do editor:

- **Save to Card:** salva os dados do fluxograma na nota do Anki.
- **Save and Generate Cards:** salva o fluxograma e gera os cartões Cloze correspondentes.

Seus cartões estarão prontos para revisão!

## ✦ ATALHOS DE TECLADO

| Atalho | Ação |
|---|---|
| `Ctrl + A` | Adicionar uma Etapa / Caixa |
| `Ctrl + B` | Adicionar uma Decisão |
| `Ctrl + C` | Adicionar um elemento de Informação |
| `Ctrl + Shift + E` | Editar o texto do elemento selecionado |
| `Ctrl + Shift + X` | Abrir anotações e imagens do Extra |
| `Ctrl + L` | Ativar ou desativar o Link Mode |
| `Ctrl + Shift + C` | Incrementar e aplicar o número Cloze |
| `Ctrl + Shift + Alt + C` | Aplicar o número Cloze atual |
| `Ctrl + Shift + F` | Ativar o Focus Flow |
| `Ctrl + S` | Salvar o fluxograma na nota do Anki |
| `Ctrl + Z` | Desfazer |
| `Ctrl + Y` / `Ctrl + Shift + Z` | Refazer |
| `Ctrl + +` / `Ctrl + -` | Aumentar / diminuir o zoom |
| `Ctrl + 0` | Restaurar o zoom para 100% |
| `Ctrl + 9` | Enquadrar todo o fluxograma na tela |
| `Ctrl + Roda do Mouse` | Aplicar zoom ao redor do cursor |
| `Delete` | Excluir elemento ou seta selecionada |
| `Ctrl + Shift + Delete` | Limpar todo o fluxograma |
| `Enter / F2` | Editar o rótulo da seta selecionada |
| `Escape` | Cancelar o Link Mode |

**Formatação de texto:** `Ctrl + B` Negrito · `Ctrl + I` Itálico · `Ctrl + U` Sublinhado.

**Interações adicionais:**

- Dê dois cliques em um elemento para editar seu texto ou em uma seta para editar seu rótulo.
- Arraste os elementos para reposicioná-los.
- Arraste o fundo vazio para movimentar a área de trabalho.
- Arraste os pontos azuis de conexão para conectar elementos.
- Utilize `Shift + Clique` ou `Shift + Arraste` para selecionar várias caixas.
- Altere simultaneamente o tipo das caixas selecionadas.
- Utilize `Ctrl + V` para colar imagens no editor ou no conteúdo Extra.

*No macOS, utilize Command (⌘) em vez de Ctrl nos atalhos compatíveis com a tecla Meta.*

## ✦ PARA QUEM É O MEDFLOW?

Ideal para estudantes de Medicina, estudantes de Enfermagem e profissionais da saúde que estudam:

- 🧠 Algoritmos diagnósticos e diagnósticos diferenciais.
- 💊 Protocolos terapêuticos e diretrizes clínicas.
- 🫀 Fisiopatologia e progressão das doenças.
- 🚑 Algoritmos de medicina de emergência.
- ⚖️ Tomada de decisão clínica.
- 🔬 Anatomia, histologia, patologia e radiologia.
- 📊 Qualquer assunto que se beneficie da organização visual.

Porém quaquer aluno que goste de fluxogramas pode utilizar

## ✦ COMPATIBILIDADE

- Anki Desktop.
- Windows, macOS e Linux.
- Suporte a PyQt5 e PyQt6.
- Compatibilidade com o modo escuro do Anki.
- Os cartões gerados podem ser revisados em clientes Anki compatíveis, incluindo AnkiMobile e AnkiWeb.

## ✦ DESENVOLVIMENTO, IA E AGRADECIMENTOS

O MEDFlow foi desenvolvido de forma independente, tendo como inspiração o projeto **ZeestMedical**. Reconhecemos e agradecemos aos desenvolvedores e colaboradores originais pelo trabalho realizado.

Ferramentas de **Inteligência Artificial (IA)** foram utilizadas ao longo do desenvolvimento para auxiliar na programação, geração de código, depuração, identificação de erros, implementação de funcionalidades e melhorias na experiência do usuário.

O conceito, a direção e o desenvolvimento do projeto foram conduzidos de forma independente, com as tecnologias de IA atuando como ferramentas de apoio durante sua criação.

---

**MEDFlow – Pense Visualmente. Aprenda Ativamente. Memorize Mais. 🧠✨**