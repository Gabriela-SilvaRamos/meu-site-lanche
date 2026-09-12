import streamlit as st

# 1. Configurações da página
st.set_page_config(page_title="Pergunta Importante", page_icon="❤️", layout="centered")

# 2. Inicializa a memória do "Sim"
if "aceitou" not in st.session_state:
    st.session_state.aceitou = False

# Estilos CSS estáveis para o fundo cinza
st.markdown("""
    <style>
    .stApp { background-color: #f0f0f0; }
    #MainMenu, footer, header { visibility: hidden; }
    
    /* Painel fixo da barra de progresso */
    .painel-tristeza {
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 80%;
        max-width: 500px;
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        text-align: center;
        z-index: 999;
        font-family: Arial;
    }
    .barra-container {
        width: 100%;
        background-color: #e0e0e0;
        border-radius: 5px;
        margin-top: 10px;
        overflow: hidden;
    }
    .barra-progresso {
        width: 0%;
        height: 15px;
        background-color: #f44336;
        transition: width 0.3s ease;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Título (A Pergunta)
st.markdown("<br><h1 style='text-align: center; color: black; font-family: Arial;'>Você aceita comer um lanche comigo?</h1><br>", unsafe_allow_html=True)

# 4. Tela de Sucesso (Se clicou em SIM)
if st.session_state.aceitou:
    # Código HTML que cria a chuva de corações reais caindo do topo
    chuva_coracoes_html = """
    <div style='padding:20px; border-radius:10px; background-color:#d4edda; color:#155724; text-align:center; font-size:24px; font-weight:bold; font-family:Arial;'>
        Sabia que você ia aceitar! ❤️ Você paga!!
    </div>
    
    <div id="chuva-container" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: 9999; overflow: hidden;"></div>

    <script>
        const container = document.getElementById('chuva-container');
        
        function criarCoracao() {
            const coracao = window.parent.document.createElement('div');
            coracao.innerText = '❤️';
            coracao.style.position = 'fixed';
            coracao.style.top = '-50px';
            coracao.style.left = Math.random() * 100 + 'vw';
            coracao.style.fontSize = (Math.random() * 20 + 15) + 'px';
            coracao.style.transition = 'transform ' + (Math.random() * 3 + 2) + 's linear, opacity 2s';
            coracao.style.pointerEvents = 'none';
            coracao.style.zIndex = '9999';
            
            window.parent.document.body.appendChild(coracao);
            
            // Faz o coração cair animado
            setTimeout(() => {
                coracao.style.transform = 'translateY(' + (window.parent.innerHeight + 100) + 'px) rotate(' + (Math.random() * 360) + 'deg)';
            }, 50);
            
            // Remove o coração depois que ele passa da tela
            setTimeout(() => {
                coracao.remove();
            }, 5000);
        }
        
        // Cria corações sem parar a cada 100 milissegundos
        setInterval(criarCoracao, 100);
    </script>
    """
    st.components.v1.html(chuva_coracoes_html, height=200)

# 5. Jogo Ativo
else:
    # Jogo integrado com o painel de tristeza e fuga
    jogo_html = """
    <div id="container-botoes" style="display: flex; justify-content: center; gap: 20px; margin-top: 20px; height: 250px; position: relative; font-family: Arial;">
        <button id="btn-sim" style="padding: 10px 30px; font-size: 18px; background-color: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; height: 45px; z-index: 10;">
            Sim
        </button>
        <button id="btn-nao" style="padding: 10px 30px; font-size: 18px; background-color: #f44336; color: white; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; height: 45px; position: relative; transition: all 0.1s ease; z-index: 10;">
            Não
        </button>
    </div>

    <div class="painel-tristeza">
        <p id="texto-porcentagem" style="margin: 0 0 5px 0; color: #555; font-weight: bold;">
            Nível de tristeza por você tentar clicar no Não: 0%
        </p>
        <p id="frase-drama" style="margin: 0 0 10px 0; font-size: 14px; font-style: italic; color: #777;">
            "Tudo na paz por enquanto... 🕊️"
        </p>
        <div class="barra-container">
            <div id="minha-barra" class="barra-progresso"></div>
        </div>
    </div>

    <script>
        const btnSim = document.getElementById('btn-sim');
        const btnNao = document.getElementById('btn-nao');
        const barra = document.getElementById('minha-barra');
        const textoPct = document.getElementById('texto-porcentagem');
        const fraseDrama = document.getElementById('frase-drama');
        const app = window.parent.document.querySelector('.stApp');

        let nivelTristeza = 0;

        const frases = {
            0: "Tudo na paz por enquanto... 🕊️",
            10: "Poxa, já tentou clicar no Não? 😢",
            20: "Sério isso? Duas vezes? Quer que eu chore? 💔",
            30: "Meu coração está quebrando... 🥺",
            40: "Tô começando a achar que você não quer o lanche... 😭",
            50: "Metade do meu coração já era. 📉",
            60: "Por que você é assim? Você não me ama é? 💔💔",
            70: "Desiste de clicar aí, poxa! 🛑",
            80: "EU SEI QUE SOU UM LIXO PRA VOCÊ! 😭",
            90: "ÚLTIMA CHANCE DE CLICAR NO SIM! ⚠️",
            100: "TRISTEZA MÁXIMA ATINGIDA! Vou chorar no banho. 💔😭😭"
        };

        function tremerTela() {
            app.style.animation = 'none';
            setTimeout(() => { app.style.animation = 'treme 0.2s 2'; }, 10);
        }

        if (!window.parent.document.getElementById('style-tremor')) {
            const style = window.parent.document.createElement('style');
            style.id = 'style-tremor';
            style.innerHTML = `@keyframes treme { 0% { transform: translate(3px, 3px); } 50% { transform: translate(-3px, -3px); } 100% { transform: translate(3px, 3px); } }`;
            window.parent.document.head.appendChild(style);
        }

        function fugir() {
            tremerTela();
            
            const mX = Math.floor(Math.random() * 70) + 10;
            const mY = Math.floor(Math.random() * 50) + 10;
            btnNao.style.position = 'absolute';
            btnNao.style.left = mX + '%';
            btnNao.style.top = mY + '%';
            
            if (nivelTristeza < 100) {
                nivelTristeza += 10;
                barra.style.width = nivelTristeza + '%';
                textoPct.innerText = `Nível de tristeza por você tentar clicar no Não: ${nivelTristeza}%`;
                fraseDrama.innerText = `"${frases[nivelTristeza]}"`;
            }
        }

        btnNao.addEventListener('click', fugir);
        btnNao.addEventListener('mouseover', fugir);

        btnSim.addEventListener('click', function() {
            const campoSecreto = window.parent.document.querySelector('.stButton button');
            if (campoSecreto) campoSecreto.click();
        });
    </script>
    """
    st.components.v1.html(jogo_html, height=450)

    # Botão invisível do Streamlit para mudar de tela
    st.markdown("<div style='display:none;'>", unsafe_allow_html=True)
    if st.button("CliqueSecreto"):
        st.session_state.aceitou = True
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

