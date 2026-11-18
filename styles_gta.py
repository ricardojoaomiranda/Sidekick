"""GTA VI inspired look for the Sidekick app: a Vice City night, with a hot pink to sunset
orange gradient, neon purple accents and teal highlights over a dark sky.
In Gradio 6, theme, css and js are passed to launch() rather than to gr.Blocks()."""

import gradio as gr

PINK = "#FF2E88"
ORANGE = "#FF8A3D"
PURPLE = "#8B3DFF"
TEAL = "#2DE2E6"
NIGHT = "#0D0619"

THEME = gr.themes.Base(
    primary_hue=gr.themes.Color(
        c50="#FFF0F7", c100="#FFD6EA", c200="#FFADD4", c300="#FF85BF", c400="#FF5CA9",
        c500="#FF2E88", c600="#D91A6E", c700="#B01057", c800="#870A42", c900="#5E062E",
        c950="#3A031C",
    ),
    neutral_hue="slate",
    font=[gr.themes.GoogleFont("Montserrat"), "ui-sans-serif", "system-ui", "sans-serif"],
    font_mono=["JetBrains Mono", "ui-monospace", "monospace"],
)

HEADER = """
<div id="header">
    <div class="sun"></div>
    <div class="header-text">
        <div class="context-label">Vice City &middot; Your personal co-worker</div>
        <h1>Sidekick<span class="vi">VI</span></h1>
        <div class="brand-bar"></div>
    </div>
</div>
"""

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Anton&display=swap');

body, .gradio-container {
    background:
        radial-gradient(120% 60% at 50% 0%, rgba(255, 46, 136, 0.28) 0%, rgba(255, 46, 136, 0) 60%),
        radial-gradient(90% 50% at 85% 100%, rgba(139, 61, 255, 0.30) 0%, rgba(139, 61, 255, 0) 70%),
        radial-gradient(70% 45% at 0% 90%, rgba(45, 226, 230, 0.14) 0%, rgba(45, 226, 230, 0) 70%),
        linear-gradient(180deg, #1A0B2E 0%, #0D0619 55%, #07030F 100%) !important;
    background-attachment: fixed !important;
    color: #F5E9FF !important;
}

/* === HEADER: sunset card === */
#header {
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: center;
    gap: 22px;
    padding: 22px 26px;
    border-radius: 18px;
    background: linear-gradient(115deg, #2A0F45 0%, #5B1466 45%, #B3245F 78%, #FF8A3D 100%);
    box-shadow: 0 10px 40px -10px rgba(255, 46, 136, 0.55), inset 0 0 0 1px rgba(255, 255, 255, 0.08);
}

#header::after {
    content: "";
    position: absolute;
    inset: auto 0 0 0;
    height: 45%;
    background: repeating-linear-gradient(0deg, rgba(13, 6, 25, 0.35) 0 3px, transparent 3px 9px);
    pointer-events: none;
}

#header .sun {
    flex: none;
    width: 64px;
    height: 64px;
    border-radius: 50%;
    background: linear-gradient(180deg, #FFD36B 0%, #FF8A3D 45%, #FF2E88 100%);
    box-shadow: 0 0 30px rgba(255, 138, 61, 0.7);
    -webkit-mask: repeating-linear-gradient(180deg, #000 0 7px, transparent 7px 10px);
    mask: repeating-linear-gradient(180deg, #000 0 7px, transparent 7px 10px);
}

#header .header-text { position: relative; z-index: 1; }

#header .context-label {
    color: #FFD6EA;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.32em;
    text-transform: uppercase;
    opacity: 0.85;
}

#header h1 {
    font-family: "Anton", "Impact", sans-serif !important;
    font-style: italic;
    font-weight: 400;
    font-size: 46px;
    line-height: 1;
    letter-spacing: 0.02em;
    text-transform: uppercase;
    margin: 6px 0 10px;
    color: #FFFFFF !important;
    text-shadow: 0 0 18px rgba(255, 46, 136, 0.65), 3px 3px 0 #1A0B2E;
}

#header h1 .vi {
    margin-left: 12px;
    background: linear-gradient(180deg, #FFD36B 0%, #FF8A3D 40%, #FF2E88 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    text-shadow: none;
    filter: drop-shadow(3px 3px 0 #1A0B2E);
}

#header .brand-bar {
    height: 4px;
    width: 160px;
    border-radius: 2px;
    background: linear-gradient(90deg, #2DE2E6 0%, #8B3DFF 40%, #FF2E88 75%, #FF8A3D 100%);
    box-shadow: 0 0 12px rgba(255, 46, 136, 0.6);
}

/* === PANELS: dark glass with neon edge === */
#chat, #plan-panel, #ask-panel {
    background: rgba(26, 11, 46, 0.72) !important;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 46, 136, 0.35) !important;
    border-radius: 16px !important;
    box-shadow: 0 0 0 1px rgba(139, 61, 255, 0.15), 0 12px 40px -18px rgba(255, 46, 136, 0.5) !important;
}

#chat .message, #chat .message * { font-size: 14px; color: #F5E9FF !important; }

#chat [data-testid="user"], #chat .message.user {
    background: linear-gradient(135deg, #FF2E88 0%, #B3245F 100%) !important;
    border: none !important;
}

#chat [data-testid="bot"], #chat .message.bot {
    background: rgba(45, 226, 230, 0.08) !important;
    border: 1px solid rgba(45, 226, 230, 0.35) !important;
}

#chat label, #chat .label-wrap span {
    color: #FF85BF !important;
    font-weight: 700;
    letter-spacing: 0.15em;
    text-transform: uppercase;
}

/* === PLAN PANEL: mission list === */
#plan-panel { padding: 16px 18px; }
#plan-panel h3 {
    font-family: "Anton", "Impact", sans-serif !important;
    font-style: italic;
    font-weight: 400;
    color: #FF8A3D !important;
    font-size: 20px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin: 0 0 10px;
    text-shadow: 0 0 10px rgba(255, 138, 61, 0.5);
}
#plan-panel .placeholder { color: #B79CCF; font-size: 13px; font-style: italic; }
#plan-panel ul { list-style: none; padding: 0; margin: 0; }
#plan-panel li {
    color: #F5E9FF;
    font-size: 13px;
    line-height: 1.45;
    margin: 8px 0;
    display: flex;
    align-items: baseline;
    gap: 8px;
}
#plan-panel .mark {
    flex: none;
    width: 12px;
    height: 12px;
    transform: rotate(45deg);
    position: relative;
    top: 1px;
}
#plan-panel li.pending .mark { border: 2px solid #8B3DFF; background: transparent; }
#plan-panel li.in_progress .mark {
    border: 2px solid #2DE2E6;
    background: #2DE2E6;
    box-shadow: 0 0 10px #2DE2E6;
}
#plan-panel li.completed .mark {
    border: 2px solid #FF8A3D;
    background: #FF8A3D;
    box-shadow: 0 0 8px rgba(255, 138, 61, 0.7);
}
#plan-panel li.completed { color: #B79CCF; text-decoration: line-through; }

/* === INPUTS === */
#ask-panel { padding: 6px; }
#ask-panel, #ask-panel > div, #ask-panel .block, #ask-panel .form {
    background: transparent !important;
    border-color: transparent !important;
}
#ask-panel textarea, #ask-panel input {
    background: rgba(13, 6, 25, 0.7) !important;
    color: #F5E9FF !important;
    border: 1px solid rgba(139, 61, 255, 0.45) !important;
    border-radius: 10px !important;
    font-size: 14px;
}
#ask-panel textarea:focus, #ask-panel input:focus {
    border-color: #FF2E88 !important;
    box-shadow: 0 0 0 3px rgba(255, 46, 136, 0.25) !important;
}
#ask-panel textarea::placeholder { color: #8E78A8 !important; }

/* === BUTTONS === */
#go-button, #approve-button, #reset-button {
    font-family: "Anton", "Impact", sans-serif !important;
    font-style: italic;
    font-weight: 400 !important;
    font-size: 18px !important;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    border-radius: 10px !important;
    transition: transform 0.1s, box-shadow 0.15s, filter 0.15s !important;
}
#go-button {
    background: linear-gradient(90deg, #FF2E88 0%, #FF8A3D 100%) !important;
    color: #FFFFFF !important;
    border: none !important;
    box-shadow: 0 0 18px rgba(255, 46, 136, 0.55) !important;
}
#go-button:hover { filter: brightness(1.1); transform: translateY(-1px); }
#go-button:disabled { filter: grayscale(0.7) brightness(0.6); box-shadow: none !important; }
#approve-button {
    background: linear-gradient(90deg, #2DE2E6 0%, #8B3DFF 100%) !important;
    color: #FFFFFF !important;
    border: none !important;
    box-shadow: 0 0 18px rgba(45, 226, 230, 0.5) !important;
}
#approve-button:hover { filter: brightness(1.1); transform: translateY(-1px); }
#reset-button {
    background: transparent !important;
    color: #FF85BF !important;
    border: 1px solid rgba(255, 46, 136, 0.6) !important;
}
#reset-button:hover { background: rgba(255, 46, 136, 0.15) !important; color: #FFFFFF !important; }

footer { display: none !important; }
"""

# The look is a night scene, so force Gradio's dark mode regardless of the system setting.
# Served via launch(head=JS), so it runs before the app mounts and there is no light flash.
JS = """
<script>
    const url = new URL(window.location);
    if (url.searchParams.get('__theme') !== 'dark') {
        url.searchParams.set('__theme', 'dark');
        window.location.replace(url.href);
    }
</script>
"""
