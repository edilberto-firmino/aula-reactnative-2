from pathlib import Path
import html
import re
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
asset = ROOT / 'exemplo/assets/evento.png'
asset.parent.mkdir(parents=True, exist_ok=True)
im = Image.new('RGB', (1200, 600), '#122542')
d = ImageDraw.Draw(im)
d.ellipse((850, -180, 1350, 320), fill='#1d4ed8')
d.ellipse((950, 50, 1120, 220), fill='#8fd4ff')
d.rounded_rectangle((80, 90, 700, 510), 30, fill='#203b62', outline='#8fd4ff', width=3)
font = 'C:/Windows/Fonts/arialbd.ttf'
d.text((125, 135), 'CAMPUS', font=ImageFont.truetype(font, 32), fill='#8fd4ff')
d.text((125, 210), 'IDEIAS QUE', font=ImageFont.truetype(font, 62), fill='white')
d.text((125, 285), 'CONECTAM', font=ImageFont.truetype(font, 62), fill='white')
d.text((125, 405), 'ENCONTRO DE TECNOLOGIA', font=ImageFont.truetype(font, 27), fill='#cbd5e1')
im.save(asset)

old = (ROOT.parent / 'aula-pratica-1/aula-reactnative/index.html').read_text(encoding='utf-8-sig')
css = re.search(r'<style>(.*?)</style>', old, re.S).group(1)
css += '\n.preview{max-width:360px;margin:24px auto;background:#eff6ff;padding:22px;border:7px solid #122542;border-radius:28px}.preview img{width:100%;display:block}.preview article{background:white;border:1px solid #dbe4ef;border-radius:16px;overflow:hidden}.preview .inside{padding:18px}.preview h3{margin:10px 0;font-size:23px}.preview p{font-size:15px}.preview .demo{display:block;width:100%;background:#1d4ed8;color:white;padding:14px;margin-top:16px}.preview small{color:#475569}.table-scroll{overflow-x:auto}.result{background:#ecfdf5;border-left:4px solid #059669;padding:14px 18px;margin:18px 0}.step{font-weight:700;color:#1d4ed8}details{margin:16px 0}summary{cursor:pointer;font-weight:700}.back{display:inline-block;margin-top:16px}@media print{.preview{break-inside:avoid}.code{break-inside:auto}nav{display:none}}'
sections = []
def code(label, text, download=None):
    extra = f'<a href="{download}" download>Baixar arquivo</a>' if download else ''
    return f'<div class="code"><div class="bar"><strong>{html.escape(label)}</strong><div><button type="button" class="copy">Copiar</button>{extra}</div></div><pre><code>{html.escape(text)}</code></pre></div>'
def section(id, title, body):
    sections.append((id, title, f'<section id="{id}"><h2>{title}</h2>{body}<a class="back" href="#sumario">Voltar ao roteiro ↑</a></section>'))
def note(text): return f'<div class="note">{text}</div>'
def result(text): return f'<div class="result"><strong>O que você deve ver:</strong> {text}</div>'

section('objetivo', '01 · O que vamos construir nesta aula', '''
<p>Na primeira prática, você preparou o ambiente e abriu uma tela simples. Agora vai transformar essa base em uma tela de apresentação de um evento fictício, usando <strong>React Native, Expo e JavaScript</strong>.</p>
<p>Ao final, você deverá identificar componentes, organizar estilos, exibir uma imagem local, passar dados por propriedades e responder ao toque em um botão. A prática pode ser individual ou em dupla.</p>
<div class="preview" aria-label="Representação aproximada da tela final"><small>EVENTOS DO CAMPUS</small><h3>Vamos aprender juntos?</h3><p>Conheça o encontro e experimente a interação.</p><article><img src="exemplo/assets/evento.png" alt="Ilustração com o texto Ideias que conectam"><div class="inside"><small>OFICINA • TECNOLOGIA</small><h3>Encontro de Tecnologia</h3><p>Data: 21 de outubro de 2026, às 19h</p><p>Local: Auditório do campus</p><p>Uma conversa sobre aplicativos, criatividade e soluções para o dia a dia.</p><button class="demo" id="demo" type="button">Tenho interesse</button><p id="demo-result" role="status"></p></div></article><p><small>Evento fictício para fins didáticos.</small></p></div>
<p>A representação acima é uma prévia HTML do resultado, não o aplicativo React Native. Toque no botão para conhecer a mensagem de simulação. A aparência do alerta real depende da plataforma.</p>
<p><strong>Escopo:</strong> uma tela, um cartão e uma interação. Não há inscrição real, envio de dados, login, banco de dados ou navegação nesta prática.</p>''')

section('roteiro', '02 · Como acompanhar a prática', '''
<table><tr><th>Etapa</th><th>O que você fará</th><th>Resultado</th></tr><tr><td>Preparar</td><td>Conferir ferramentas e escolher o projeto.</td><td>Tela inicial abre no aparelho.</td></tr><tr><td>Construir</td><td>Criar três arquivos e copiar a imagem.</td><td>Cartão do evento aparece.</td></tr><tr><td>Entender</td><td>Relacionar JSX, dados, props, estilos e eventos.</td><td>Explica o funcionamento do botão.</td></tr><tr><td>Personalizar</td><td>Alterar evento, cores e identificação.</td><td>Tela própria e legível.</td></tr><tr><td>Verificar</td><td>Testar toque, rolagem e fonte ampliada.</td><td>Entrega com evidências reais.</td></tr></table>
<p>Sugestão para um encontro de duas horas: 15 minutos de retomada, 20 de preparação, 40 de construção, 25 de personalização e 20 de testes e explicação. Instalações demoradas podem exigir preparação anterior.</p>''')

section('ferramentas', '03 · Instalar e conferir as ferramentas', '''
<ol><li>Instale <a href="https://nodejs.org/">Node.js LTS</a>, incluindo npm e a opção de PATH do instalador.</li><li>Instale <a href="https://code.visualstudio.com/">Visual Studio Code</a>.</li><li>No celular, instale Expo Go conforme <a href="https://expo.dev/go">expo.dev/go</a>.</li><li>Feche e reabra o terminal após instalar Node.js. No VS Code, use Terminal → Novo Terminal.</li></ol>
''' + code('Terminal — verificação', 'node --version\nnpm --version') + result('duas versões, uma do Node.js e outra do npm. Os números podem ser diferentes dos apresentados pelo professor.') + '''
<p>O projeto encontrado na primeira prática usa Expo SDK 57. A <a href="https://docs.expo.dev/versions/v57.0.0/">tabela oficial desse SDK</a> informa Node.js mínimo 22.13.x. Se criar outro SDK, confira o requisito correspondente. Não altere as versões do projeto apenas para reproduzir um número deste manual.</p>
''' + note('Quem já possui ferramentas funcionando pode apenas conferir as versões. Não é necessário instalar a antiga CLI global <code>expo-cli</code>. Android Studio é opcional quando você usa celular com Expo Go. O computador e o celular precisam conseguir se comunicar pela rede.'))

section('projeto', '04 · Escolher: continuar ou criar um projeto', '''
<h3>Caminho A — Continuar a primeira prática</h3><p>Faça uma cópia de segurança de <code>App.js</code> e de outros arquivos que pretende substituir, fora da pasta do projeto. Abra <code>minhas-tarefas-expo</code> no VS Code. No terminal da pasta INBEC:</p>
''' + code('Terminal — projeto existente', 'cd minhas-tarefas-expo\nnpm install') + '''
<p><code>npm install</code> recupera dependências a partir do projeto; é útil quando elas ainda não estão instaladas. Se você já está dentro da pasta do aplicativo, não execute o <code>cd</code> novamente.</p>
<h3>Caminho B — Começar um projeto separado</h3><p>No terminal de sua pasta de trabalho, execute:</p>
''' + code('Terminal — novo projeto', 'npx create-expo-app@latest eventos-campus --template blank\ncd eventos-campus') + '''
<p>Se o npm solicitar autorização para baixar o gerador, responda <code>y</code> e aguarde o término. Abra a pasta <code>eventos-campus</code> no VS Code por Arquivo → Abrir Pasta.</p>
''' + result('arquivos como App.js, index.js, app.json e package.json, além da pasta assets. O nome da pasta depende do caminho escolhido.') + note('Escolha somente um caminho. Esta prática utiliza o template <code>blank</code> em JavaScript, com <code>App.js</code>. Se seu projeto tem <code>src/app</code>, arquivos <code>.tsx</code> ou Expo Router, peça orientação antes de copiar: a entrada é diferente. A pasta do manual <code>aula-pratica-2</code> não é a raiz de um aplicativo Expo.'))

section('bibliotecas', '05 · Instalar as bibliotecas e abrir a base', '''
<p>Dentro da pasta que contém o <code>package.json</code> do aplicativo, execute:</p>
''' + code('Terminal — bibliotecas da aula', 'npx expo install react-native-safe-area-context expo-status-bar') + '''
<table><tr><th>Biblioteca</th><th>Por que usamos</th></tr><tr><td>react-native-safe-area-context</td><td>Reserva áreas ocupadas por recortes e barras do sistema.</td></tr><tr><td>expo-status-bar</td><td>Configura o estilo visual da barra de status.</td></tr></table>
<p>Use <code>expo install</code> para resolver versões adequadas ao SDK. O gerador já inclui React, React Native e Expo; não instale esses pacotes separadamente. AsyncStorage não é necessário nesta aula.</p>
''' + code('Terminal — iniciar a base', 'npx expo start --go') + '''
<ol><li>Aguarde o servidor Metro e o QR code aparecerem.</li><li>No Android, abra Expo Go e a opção de ler QR code, quando disponível. No iPhone, use a câmera para abrir o link no Expo Go.</li><li>Mantenha computador e celular na mesma rede e o terminal aberto.</li><li>Confira a tela inicial antes de modificar os arquivos.</li></ol>
''' + result('a tela inicial do projeto, ou a tela que você fez na primeira prática. O QR code aparece no terminal do computador, não neste manual.') + note('Confira a versão de <code>expo</code> em <code>package.json</code> e a compatibilidade do Expo Go em <a href="https://expo.dev/go">expo.dev/go</a>. Se houver incompatibilidade, alinhe o SDK e o aplicativo com o professor. Não atualize pacotes isolados por tentativa.'))

section('estrutura', '06 · Criar os arquivos e copiar a imagem', '''
<p>No explorador do VS Code, crie a pasta <code>components</code> e os arquivos abaixo. A estrutura final dentro do seu aplicativo será:</p>
''' + code('Estrutura — não é comando de terminal', '''seu-projeto/
├── App.js
├── styles.js
├── components/
│   └── CartaoEvento.js
├── assets/
│   └── evento.png
├── app.json
├── index.js
└── package.json''') + '''
<p><a href="exemplo/assets/evento.png" download="evento.png">Baixar evento.png</a>. Salve a imagem na pasta <code>assets</code> do aplicativo com esse nome exato. Se o navegador abrir a imagem, use Salvar imagem como. Confira se não ficou <code>evento.png.png</code>.</p>
<p>Os três arquivos completos também estão na pasta <code>exemplo</code> deste material. Copie-os para os mesmos caminhos relativos no aplicativo; copie a imagem para <code>assets/evento.png</code>. A pasta <code>exemplo</code> contém apenas os arquivos da aula, sem instalação independente.</p>
<table><tr><th>Arquivo</th><th>Responsabilidade</th></tr><tr><td>App.js</td><td>Dados do evento, mensagem do botão e composição da tela.</td></tr><tr><td>components/CartaoEvento.js</td><td>Cartão que recebe dados e uma função.</td></tr><tr><td>styles.js</td><td>Objetos com estilos compartilhados.</td></tr><tr><td>assets/evento.png</td><td>Imagem local incluída no aplicativo.</td></tr></table>
''' + note('Mantenha <code>index.js</code>, <code>app.json</code> e <code>package.json</code> gerados pelo Expo. Não substitua essas configurações por arquivos de outro SDK. O <code>index.html</code> que você está lendo é material de apoio; a tela nativa será feita em JSX.'))

for id, title, path, intro in [
 ('app', '07 · Código completo de App.js', 'App.js', 'Substitua o conteúdo de App.js pelo código abaixo. O objeto evento concentra as informações fictícias; mostrarInteresse é a função acionada pelo cartão.'),
 ('cartao', '08 · Código completo de components/CartaoEvento.js', 'components/CartaoEvento.js', 'Crie este arquivo dentro de components. Ele recebe evento e onInteresse por props. O botão usa a função recebida, e os textos usam os dados do evento.'),
 ('estilos', '09 · Código completo de styles.js', 'styles.js', 'Crie styles.js na raiz, ao lado de App.js. Os nomes dos estilos correspondem aos nomes utilizados nos dois componentes.')]:
    section(id, title, f'<p>{intro}</p>' + code(path, (ROOT/'exemplo'/path).read_text(encoding='utf-8'), 'exemplo/'+path) + ('<p>Salve os três arquivos e confira se a imagem está no caminho correto antes de analisar erros de importação.</p>' if id=='estilos' else ''))

section('entender', '10 · Entender o código que você acabou de criar', '''
<table><tr><th>Conceito</th><th>Onde aparece</th><th>O que significa</th></tr><tr><td>JSX</td><td>Blocos dentro de return</td><td>Descreve a árvore da interface no JavaScript.</td></tr><tr><td>View</td><td>Conteúdo e cartão</td><td>Agrupa elementos e organiza o layout.</td></tr><tr><td>Text</td><td>Títulos e informações</td><td>Exibe conteúdo textual; não deixe texto solto em View.</td></tr><tr><td>Image</td><td>Topo do cartão</td><td>Exibe a imagem indicada em source.</td></tr><tr><td>Pressable</td><td>Tenho interesse</td><td>Responde ao toque e informa se está pressionado.</td></tr><tr><td>ScrollView</td><td>Tela principal</td><td>Permite alcançar conteúdo maior que a altura disponível.</td></tr><tr><td>Props</td><td>evento e onInteresse</td><td>Dados e função enviados de App para CartaoEvento.</td></tr><tr><td>StyleSheet.create</td><td>styles.js</td><td>Organiza estilos em objetos JavaScript.</td></tr><tr><td>SafeAreaProvider / SafeAreaView</td><td>Raiz da tela</td><td>Fornecem contexto e espaçamento para áreas seguras.</td></tr><tr><td>Platform e Alert</td><td>mostrarInteresse</td><td>Selecionam a mensagem adequada ao ambiente de execução.</td></tr></table>
<h3>O caminho de um toque</h3><p>Você toca no Pressable → ele chama onInteresse → essa prop aponta para mostrarInteresse → a função monta a mensagem com evento.nome → o sistema mostra um alerta.</p>
''' + code('Comparação — função e execução', '''// Correto: entrega a função para ser chamada no toque.
onPress={onInteresse}

// Evite: chama a função enquanto o componente é renderizado.
onPress={onInteresse()}''') + '''
<h3>Dados e caminhos</h3><p>As chaves em <code>{evento.nome}</code> inserem um valor JavaScript no JSX. O <code>require('./assets/evento.png')</code> usa um caminho literal relativo ao App.js. No cartão, <code>../styles</code> sobe uma pasta até a raiz.</p>
<h3>Estilos que serão observados</h3><p><code>padding</code> cria espaço interno; <code>marginBottom</code> separa um elemento do próximo; <code>gap</code> separa os filhos do contêiner. <code>flex: 1</code> faz a área principal ocupar o espaço disponível. <code>maxWidth</code> limita a largura de leitura, e <code>alignSelf: 'center'</code> centraliza o conteúdo em telas largas.</p>
<p>A imagem usa largura de 100% e proporção 2:1. O cartão não tem altura fixa, permitindo que textos cresçam. A opacidade do botão muda durante o toque; isso não registra interesse nem altera um estado persistente.</p>''')

section('executar', '11 · Salvar, executar e reconhecer o resultado', '''
<ol><li>Salve todos os arquivos com Ctrl+S.</li><li>Se Metro já estiver aberto, mantenha-o em execução e observe a atualização automática.</li><li>Se você fechou o servidor, abra o terminal na raiz do aplicativo e execute o comando abaixo.</li></ol>
''' + code('Terminal — retomar', 'npx expo start --go') + result('título “Vamos aprender juntos?”, imagem “Ideias que conectam”, nome do evento, data, local, descrição, botão azul e rodapé.') + '''
<ol><li>Toque em “Tenho interesse”.</li><li>No celular, confira o alerta “Interesse demonstrado”, com o nome do evento e o aviso de simulação.</li><li>Toque em “Entendi” para fechar. No navegador, o diálogo é o alerta do próprio navegador e o texto do botão depende dele.</li><li>Altere o nome em evento.nome, salve e confira a mudança no cartão e na mensagem.</li></ol>
''' + note('Fast Refresh atualiza o código no desenvolvimento. Instalação de dependências pode exigir reiniciar Metro. Se a imagem recém-criada não aparecer, pressione <code>r</code> no terminal ou reinicie com <code>npx expo start --clear</code>.'))

section('alternativas', '12 · Alternativas: navegador, emulador e túnel', '''
<h3>Navegador</h3><p>Na raiz do aplicativo, instale o suporte web e inicie:</p>
''' + code('Terminal — web opcional', 'npx expo install react-dom react-native-web @expo/metro-runtime\nnpx expo start --web') + '''
<p>Use o endereço mostrado no terminal. Reduza e aumente a janela para observar o cartão. O exemplo inclui uma mensagem para web, mas áreas seguras e comportamento de toque precisam ser conferidos no aparelho.</p>
<h3>Emulador Android</h3><ol><li>Instale <a href="https://developer.android.com/studio">Android Studio</a> e conclua a configuração do SDK.</li><li>No Device Manager, crie um aparelho virtual, baixe a imagem de sistema e inicie-o.</li><li>Com Metro em execução, pressione <code>a</code> para abrir no Android. Aguarde a inicialização e siga as mensagens do Expo.</li></ol>
<p>Prepare o emulador antes da aula: o download e a primeira inicialização podem demorar. Consulte o <a href="https://docs.expo.dev/workflow/android-studio-emulator/">guia oficial de configuração Android</a>. Simulador iOS exige macOS e Xcode.</p>
<h3>Rede local bloqueada</h3><p>Se a rede impedir a comunicação, pare Metro com Ctrl+C e tente:</p>
''' + code('Terminal — túnel', 'npx expo start --go --tunnel') + '''
<p>O túnel exige internet, pode solicitar instalação de uma dependência e pode ser mais lento. Escaneie o novo QR code. Se não funcionar, registre o erro e use a alternativa disponível com o professor.</p>''')

section('experimentos', '13 · Experimentos guiados durante a aula', '''
<p>Faça uma mudança por vez, preveja o resultado e confira depois de salvar.</p>
<ol><li><strong>Texto:</strong> altere evento.nome, data, local e descricao no App.js. Observe que o componente continua sendo o mesmo.</li><li><strong>Cor:</strong> em styles.js, mude backgroundColor do botão para <code>'#166534'</code>. Preserve texto legível.</li><li><strong>Espaçamento:</strong> compare padding 12, 20 e 28 em detalhes. Explique o que mudou.</li><li><strong>Imagem:</strong> copie outro PNG ou JPG para assets, ajuste o require literal e a descrição acessível. Prefira uma imagem de proporção semelhante.</li><li><strong>Texto longo:</strong> use um nome de evento maior e uma descrição com várias linhas. Confira quebra de linha e rolagem.</li><li><strong>Botão:</strong> mude o rótulo e a mensagem de forma coerente, mantendo explícita a simulação.</li></ol>
<details><summary>Desafio opcional: exibir dois cartões</summary><p>Crie outro objeto de evento no App.js, com nome, data, local, descricao e imagem. Renderize outro CartaoEvento passando esse objeto. Para que a mensagem use o nome correto, faça mostrarInteresse receber o evento selecionado e passe uma função como <code>onInteresse={() =&gt; mostrarInteresse(outroEvento)}</code>. Ajuste também o primeiro cartão para passar seu evento. Use uma View com <code>gap</code> para separar os cartões.</p></details>''')

section('erros', '14 · Diagnóstico dos erros mais comuns', '''
<div class="table-scroll"><table><tr><th>Sintoma</th><th>O que conferir</th></tr><tr><td>node ou npm não reconhecido</td><td>Instalação, PATH e reabertura do terminal.</td></tr><tr><td>PowerShell bloqueia npm.ps1</td><td>Use npm.cmd / npx.cmd no lugar de npm / npx, ou escolha o terminal Prompt de Comando no VS Code. Não é preciso mudar a política global para acompanhar a aula.</td></tr><tr><td>package.json não encontrado</td><td>Abra o terminal na pasta do aplicativo, não na pasta do manual.</td></tr><tr><td>Unable to resolve ./components/CartaoEvento</td><td>Nome da pasta, nome do arquivo, maiúsculas e importação.</td></tr><tr><td>Unable to resolve ../styles</td><td>styles.js deve estar na raiz; o cartão fica em components.</td></tr><tr><td>Unable to resolve ./assets/evento.png</td><td>Imagem baixada no local correto, extensão e nome exatos.</td></tr><tr><td>Tela vermelha com erro de sintaxe</td><td>Leia a primeira mensagem; confira aspas, vírgulas, chaves, imports e fechamento das tags. Não copie as cercas de código.</td></tr><tr><td>Botão abre alerta sem toque</td><td>Use onPress={onInteresse}, sem executar a função no JSX.</td></tr><tr><td>QR code não conecta</td><td>Servidor aberto, rede, VPN, firewall e compatibilidade do Expo Go; tente túnel.</td></tr><tr><td>Project is incompatible</td><td>Confira o SDK em package.json e a versão suportada pelo Expo Go.</td></tr><tr><td>Conteúdo encoberto ou cortado</td><td>Confira SafeAreaProvider, SafeAreaView e ScrollView; remova alturas fixas adicionadas.</td></tr><tr><td>Web pede bibliotecas adicionais</td><td>Execute a instalação da seção 12 e reinicie Metro.</td></tr></table></div>
<p>Para conferir dependências sem aplicar correções automáticas:</p>
''' + code('Terminal — diagnóstico', 'npx expo-doctor@latest\nnpx expo install --check') + '''
<p>Leia o diagnóstico com o professor. Corrija o problema apontado antes de instalar novas versões. Registre a mensagem exata, o arquivo afetado e a ação que resolveu.</p>''')

section('atividade', '15 · Atividade: seu evento no campus', '''
<p><strong>Situação:</strong> sua equipe precisa apresentar uma oficina, palestra ou encontro fictício em uma tela para celular.</p>
<ol><li>Escolha um evento e personalize nome, data, local e descrição.</li><li>Troque a imagem por outra adequada ao tema, mantendo-a local.</li><li>Personalize a cor do botão e o título da página.</li><li>Inclua os nomes dos integrantes no rodapé.</li><li>Mantenha a mensagem do botão vinculada ao nome do evento e o aviso de simulação.</li><li>Teste a tela e explique a função de cada arquivo.</li></ol>
<h3>Perguntas para responder</h3><ol><li>Qual a diferença entre o index.html deste manual e o App.js do aplicativo?</li><li>Para que servem View, Text, Image e Pressable?</li><li>Quais props App envia para CartaoEvento?</li><li>Por que onPress recebe uma função?</li><li>Qual a diferença observada entre padding e margin?</li><li>Por que o alerta não representa uma inscrição salva?</li><li>Qual teste foi realizado no aparelho e qual ainda está pendente?</li></ol>
<h3>Entrega</h3><p>Envie App.js, styles.js, components/CartaoEvento.js, a imagem utilizada, package.json e package-lock.json; duas capturas (tela e mensagem do botão); as respostas e um registro de dificuldade ou verificação realizada. Identifique se as capturas vieram de celular, emulador ou navegador. Não é necessário enviar node_modules.</p>
<p>O professor define o prazo e a pontuação. Se não houver aparelho disponível, registre a execução web e deixe o teste nativo identificado como pendente.</p>''')

section('checklist', '16 · Testes e checklist antes de entregar', '''
<table><tr><th>Teste</th><th>Resultado esperado</th></tr><tr><td>Abrir a tela</td><td>Imagem, nome, data, local, descrição e rodapé aparecem.</td></tr><tr><td>Tocar no botão</td><td>Mensagem inclui o nome correto e o aviso de simulação.</td></tr><tr><td>Fechar a mensagem</td><td>Retorna à mesma tela sem inscrição real.</td></tr><tr><td>Trocar o nome e salvar</td><td>Cartão e próxima mensagem usam o novo nome.</td></tr><tr><td>Descrição longa / tela pequena</td><td>Conteúdo pode ser alcançado por rolagem.</td></tr><tr><td>Aumentar a fonte no sistema</td><td>Textos quebram linha; botão continua alcançável.</td></tr><tr><td>Janela web larga e estreita</td><td>Conteúdo acompanha a largura e respeita o limite.</td></tr><tr><td>Recortes e barras no celular</td><td>Nenhum controle essencial fica encoberto.</td></tr></table>
<p>Registre cada teste como realizado ou pendente, incluindo plataforma, resultado e ajuste necessário. A imagem é local e não exige um servidor de imagens; Expo Go ainda pode precisar da conexão com Metro para carregar o projeto.</p>
<ul class="checks">''' + ''.join(f'<li><label><input type="checkbox"> {t}</label></li>' for t in ['Ferramentas e SDK conferidos.', 'App.js, styles.js e CartaoEvento.js nos caminhos corretos.', 'Imagem local presente e descrição acessível coerente.', 'Tela personalizada e nomes no rodapé.', 'Botão responde e mostra o nome do evento.', 'Rolagem e fonte ampliada verificadas.', 'Capturas identificam a plataforma utilizada.', 'Respostas e pendências registradas.']) + '''</ul>
<p>Os marcadores servem para acompanhar esta leitura e são reiniciados quando a página é recarregada.</p>''')

section('retomar', '17 · Encerrar e retomar na próxima aula', '''
<p>Salve os arquivos e pare o servidor com Ctrl+C. Preserve a pasta completa do aplicativo. Para retomar:</p>
''' + code('Terminal — abertura da próxima aula', 'cd eventos-campus\nnpx expo start --go') + '''
<p>Se continuou a primeira prática, use <code>cd minhas-tarefas-expo</code> no lugar de eventos-campus. Se já estiver na raiz do app, execute apenas o segundo comando. Em outro computador, instale dependências com npm install antes de iniciar.</p>
<p>Você construiu uma tela com componente reutilizável e interação simples. Essa base permite aprofundar layout, estado, formulários e navegação em encontros posteriores. Não é preciso gerar APK para concluir esta aula.</p>''')

section('referencias', '18 · Referências oficiais e notas do material', '''
<p>Referências consultadas em 14/10/2026. O projeto disponível da primeira prática usa SDK 57; a versão de um projeto criado com latest pode mudar. Confira sempre a documentação correspondente ao seu package.json.</p>
<ul><li><a href="https://docs.expo.dev/versions/v57.0.0/">Expo SDK 57 e requisitos de versões</a></li><li><a href="https://docs.expo.dev/more/create-expo/">create-expo-app e templates</a></li><li><a href="https://docs.expo.dev/get-started/start-developing/">Iniciar o desenvolvimento e abrir o aplicativo</a></li><li><a href="https://expo.dev/go">Expo Go e compatibilidade</a></li><li><a href="https://docs.expo.dev/develop/user-interface/safe-areas/">Áreas seguras</a></li><li><a href="https://reactnative.dev/docs/components-and-apis">Componentes React Native</a></li><li><a href="https://reactnative.dev/docs/alert">Alert</a></li><li><a href="https://reactnative.dev/docs/style">Estilos</a></li><li><a href="https://reactnative.dev/docs/pressable">Pressable</a></li><li><a href="https://react.dev/learn/passing-props-to-a-component">Props no React</a></li></ul>
<p>O manual e a imagem podem ser consultados offline. Criação do projeto, instalação e serviços de conexão precisam de internet. A prévia é ilustrativa; o professor deve ensaiar a execução nativa no ambiente da turma.</p>''')

nav = ''.join(f'<li><a href="#{id}">{title}</a></li>' for id,title,_ in sections)
script = '''
const status = document.getElementById('status');
let timer;
function notify(message) { status.textContent = message; clearTimeout(timer); timer = setTimeout(() => { status.textContent = ''; }, 3500); }
document.querySelectorAll('.copy').forEach(button => button.addEventListener('click', async () => {
  const text = button.closest('.code').querySelector('pre code').textContent;
  try {
    if (navigator.clipboard && window.isSecureContext) await navigator.clipboard.writeText(text);
    else {
      const area = document.createElement('textarea'); area.value = text;
      area.style.position = 'fixed'; area.style.opacity = '0'; document.body.append(area); area.select();
      const ok = document.execCommand('copy'); area.remove(); if (!ok) throw new Error('copy');
    }
    notify('Código copiado!');
  } catch { notify('Selecione o código e use Ctrl+C para copiar.'); }
}));
document.getElementById('print').addEventListener('click', () => window.print());
document.getElementById('demo').addEventListener('click', () => {
  document.getElementById('demo-result').textContent = 'Interesse demonstrado! Você demonstrou interesse em Encontro de Tecnologia. Esta é uma simulação: nenhuma inscrição foi enviada.';
});
'''
page = f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Aula prática 2 — Eventos do Campus com React Native e Expo</title><style>{css}</style></head>
<body><header class="hero"><div class="eyebrow">Dispositivos Móveis · Aula prática 2</div><h1>Uma ideia, uma tela, um evento.</h1><p>Manual completo para sair da tela inicial do Expo e construir um cartão de evento com imagem, estilos e interação no celular.</p><span class="pill">Iniciante</span><span class="pill">JavaScript · App.js · Expo</span><span class="pill">Professor Edilberto Firmino</span></header>
<main><nav id="sumario" aria-label="Sumário"><h2>Roteiro da aula</h2><ul>{nav}</ul><p><button id="print" type="button">Imprimir / salvar como PDF</button></p><p>Leia em sequência na primeira vez. Os botões Copiar enviam somente o código para a área de transferência.</p></nav>
{''.join(s[2] for s in sections)}
<footer>INBEC · Desenvolvimento para Dispositivos Móveis<br>Aula prática 2 · Tela de evento com React Native e Expo</footer></main><div id="status" role="status" aria-live="polite"></div><script>{script}</script></body></html>'''
(ROOT/'index.html').write_text(page, encoding='utf-8')
(ROOT/'README.md').write_text('''# Aula prática 2 — Eventos do Campus

Abra `index.html` no navegador para acompanhar o manual completo.

O roteiro cobre preparação do ambiente, criação ou retomada de projeto Expo blank em JavaScript, componentes, props, imagem local, estilos, botão com alerta, personalização, diagnóstico e entrega.

## Arquivos

- `index.html`: manual com 18 seções, códigos completos, botões de copiar e links de download.
- `exemplo/App.js`: tela e dados do evento.
- `exemplo/styles.js`: estilos compartilhados.
- `exemplo/components/CartaoEvento.js`: componente do cartão.
- `exemplo/assets/evento.png`: ilustração local da aula.
- `gerar_manual.py`: fonte de geração do manual e da imagem; requer Python e Pillow apenas se quiser regenerar o material.

A pasta `exemplo` não é um projeto Expo independente. Crie ou abra o aplicativo conforme o manual e copie os arquivos preservando os caminhos. Não é necessário Python para ler o manual ou executar o aplicativo.

O botão demonstra interesse; não registra inscrição. A prévia HTML é ilustrativa. A execução nativa deve ser ensaiada no ambiente da turma.
''', encoding='utf-8')
print(f'Manual gerado: {len(sections)} seções, {len(page)} caracteres.')
