from pathlib import Path

src = Path("/mnt/data/life-radar-widget_3.html")

html = src.read_text(encoding="utf-8")

# Replace the existing document with an enhanced self-contained Notion-friendly widget.

enhanced = r'''<!doctype html>

<html lang="pt-BR">

<head>

<meta charset="utf-8" />

<meta name="viewport" content="width=device-width, initial-scale=1" />

<title>Life Radar</title>

<style>

  :root {

    --bg: transparent;

    --panel: rgba(255,255,255,.96);

    --border: #e8e8e8;

    --text: #595959;

    --muted: #9a9a9a;

    --grid: #e6e6e6;

    --grid-strong: #dcdcdc;

    --fill: rgba(122,122,122,0.16);

    --stroke: #8c8c8c;

    --dot: #6b6b6b;

    --label: #8f8f8f;

    --scale: #c4c4c4;

    --seg-on: #4a4a4a;

    --seg-off: #d8d8d8;

    --xp: #707070;

    --icon: #a8a8a8;

    --button: #f5f5f5;

    --button-hover: #ececec;

    --font: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;

  }

  * { box-sizing: border-box; }

  html, body {

    margin: 0;

    background: var(--bg);

    font-family: var(--font);

    -webkit-font-smoothing: antialiased;

    color: var(--text);

  }

  button, input { font: inherit; }

  .widget {

    width: min(100%, 440px);

    margin: 0 auto;

    padding: 8px 14px 18px;

  }

  .topbar {

    display: flex;

    align-items: center;

    justify-content: flex-end;

    min-height: 28px;

    margin-bottom: 2px;

  }

  .icon-button {

    width: 30px;

    height: 30px;

    display: inline-grid;

    place-items: center;

    border: 1px solid transparent;

    border-radius: 8px;

    background: transparent;

    cursor: pointer;

    color: var(--icon);

    transition: .15s ease;

  }

  .icon-button:hover {

    background: var(--button);

    color: #707070;

  }

  .icon-button.active {

    background: var(--button);

    border-color: var(--border);

    color: #606060;

  }

  .chart {

    width: 100%;

    height: auto;

    display: block;

    overflow: visible;

  }

  text { font-family: var(--font); }

  .axis-label { fill: var(--label); font-size: 11px; letter-spacing: .2px; }

  .scale-label { fill: var(--scale); font-size: 9px; }

  .bars { margin-top: 10px; }

  .bar-row {

    display: flex;

    align-items: center;

    gap: 10px;

    margin: 8px 0;

  }

  .segments {

    display: flex;

    gap: 4px;

    flex: 0 0 auto;

  }

  .seg {

    width: 9px;

    height: 9px;

    border-radius: 2px;

    background: var(--seg-off);

  }

  .seg.on { background: var(--seg-on); }

  .bar-meta {

    display: flex;

    align-items: center;

    gap: 7px;

    font-size: 11px;

    color: var(--xp);

    white-space: nowrap;

  }

  .bar-meta .xp { color: #8c8c8c; }

  .bar-meta .dot-sep { color: var(--seg-on); font-size: 8px; }

  .bar-meta .lv { color: #6b6b6b; letter-spacing: .3px; }

  .editor {

    display: none;

    margin-top: 14px;

    padding: 14px;

    border: 1px solid var(--border);

    border-radius: 12px;

    background: var(--panel);

    box-shadow: 0 8px 24px rgba(0,0,0,.04);

  }

  .editor.open { display: block; }

  .editor-title {

    font-size: 12px;

    font-weight: 600;

    color: #666;

    margin: 0 0 12px;

  }

  .axis-editor {

    display: grid;

    grid-template-columns: minmax(0, 1fr) 84px;

    align-items: center;

    gap: 10px;

    margin: 10px 0;

  }

  .axis-name {

    min-width: 0;

    font-size: 12px;

    color: #707070;

    overflow: hidden;

    text-overflow: ellipsis;

    white-space: nowrap;

  }

  .score-control {

    display: grid;

    grid-template-columns: 1fr 34px;

    align-items: center;

    gap: 8px;

  }

  input[type="range"] {

    width: 100%;

    accent-color: #777;

  }

  .score-number {

    width: 34px;

    padding: 4px 3px;

    text-align: center;

    border: 1px solid var(--border);

    border-radius: 6px;

    color: #666;

    background: white;

  }

  .editor-actions {

    display: flex;

    gap: 8px;

    margin-top: 14px;

  }

  .action-button {

    border: 1px solid var(--border);

    background: var(--button);

    color: #666;

    border-radius: 7px;

    padding: 7px 10px;

    cursor: pointer;

    font-size: 11px;

  }

  .action-button:hover { background: var(--button-hover); }

  .save-state {

    margin-left: auto;

    align-self: center;

    font-size: 10px;

    color: #a0a0a0;

  }

  @media (prefers-color-scheme: dark) {

    :root {

      --panel: rgba(32,32,32,.98);

      --border: #3b3b3b;

      --text: #d0d0d0;

      --muted: #909090;

      --grid: #3a3a3a;

      --grid-strong: #4a4a4a;

      --fill: rgba(190,190,190,.12);

      --stroke: #aaa;

      --dot: #bdbdbd;

      --label: #9d9d9d;

      --scale: #666;

      --seg-on: #c2c2c2;

      --seg-off: #4a4a4a;

      --xp: #aaa;

      --icon: #8f8f8f;

      --button: #2f2f2f;

      --button-hover: #383838;

    }

    .score-number {

      background: #292929;

      color: #d0d0d0;

    }

  }

</style>

</head>

<body>

<div class="widget">

  <div class="topbar">

    <button id="toggle-editor" class="icon-button" aria-label="Editar Life Radar" title="Editar">

      <svg width="17" height="17" viewBox="0 0 24 24" fill="none"

           stroke="currentColor" stroke-width="1.7" stroke-linecap="round">

        <line x1="4" y1="8" x2="20" y2="8"/>

        <circle cx="9" cy="8" r="2.4" fill="var(--panel)"/>

        <line x1="4" y1="16" x2="20" y2="16"/>

        <circle cx="15" cy="16" r="2.4" fill="var(--panel)"/>

      </svg>

    </button>

  </div>

  <svg class="chart" viewBox="0 0 360 320" aria-label="Gráfico radar de áreas da vida"></svg>

  <div class="bars">

    <div id="bar-list"></div>

  </div>

  <section id="editor" class="editor" aria-label="Editor do Life Radar">

    <p class="editor-title">Atualize suas áreas</p>

    <div id="axis-editor-list"></div>

    <div class="editor-actions">

      <button id="reset-button" class="action-button" type="button">Restaurar</button>

      <button id="export-button" class="action-button" type="button">Copiar dados</button>

      <span id="save-state" class="save-state">Salvo neste navegador</span>

    </div>

  </section>

</div>

<script>

const DEFAULT_CONFIG = {

  max: 5,

  axes: [

    { label: "Criatividade", value: 5 },

    { label: "Financeiro", value: 2 },

    { label: "Saúde", value: 5 },

    { label: "Aprendizado", value: 0 },

    { label: "Social", value: 5 },

    { label: "Escrita", value: 1.5 }

  ],

  bars: [

    { filled: 8, segments: 11, current: 1556, total: 1570, level: "LV5" },

    { filled: 8, segments: 11, current: 607, total: 638, level: "LV2" }

  ]

};

const STORAGE_KEY = "life-radar-widget-v1";

let config = loadConfig();

function clone(value) {

  return JSON.parse(JSON.stringify(value));

}

function loadConfig() {

  try {

    const saved = localStorage.getItem(STORAGE_KEY);

    if (!saved) return clone(DEFAULT_CONFIG);

    const parsed = JSON.parse(saved);

    if (!parsed || !Array.isArray(parsed.axes)) return clone(DEFAULT_CONFIG);

    return {

      ...clone(DEFAULT_CONFIG),

      ...parsed,

      axes: parsed.axes.map((axis, index) => ({

        label: axis.label || DEFAULT_CONFIG.axes[index]?.label || `Área ${index + 1}`,

        value: Number.isFinite(Number(axis.value)) ? Number(axis.value) : 0

      }))

    };

  } catch {

    return clone(DEFAULT_CONFIG);

  }

}

function saveConfig() {

  localStorage.setItem(STORAGE_KEY, JSON.stringify(config));

  const state = document.getElementById("save-state");

  state.textContent = "Salvo";

  clearTimeout(saveConfig.timer);

  saveConfig.timer = setTimeout(() => state.textContent = "Salvo neste navegador", 900);

}

function svgElement(tag, attrs = {}) {

  const NS = "http://www.w3.org/2000/svg";

  const el = document.createElementNS(NS, tag);

  Object.entries(attrs).forEach(([key, value]) => el.setAttribute(key, value));

  return el;

}

function renderChart() {

  const svg = document.querySelector(".chart");

  svg.replaceChildren();

  const cx = 180;

  const cy = 150;

  const R = 110;

  const n = config.axes.length;

  const max = config.max;

  const angle = i => (-90 + i * (360 / n)) * Math.PI / 180;

  const point = (i, r) => [

    cx + r * Math.cos(angle(i)),

    cy + r * Math.sin(angle(i))

  ];

  for (let level = 1; level <= max; level++) {

    const r = (R * level) / max;

    const pts = config.axes.map((_, i) => {

      const [x, y] = point(i, r);

      return `${x.toFixed(2)},${y.toFixed(2)}`;

    });

    svg.appendChild(svgElement("polygon", {

      points: pts.join(" "),

      fill: "none",

      stroke: level === max ? "var(--grid-strong)" : "var(--grid)",

      "stroke-width": 1

    }));

  }

  config.axes.forEach((_, i) => {

    const [x, y] = point(i, R);

    svg.appendChild(svgElement("line", {

      x1: cx,

      y1: cy,

      x2: x.toFixed(2),

      y2: y.toFixed(2),

      stroke: "var(--grid)",

      "stroke-width": 1

    }));

  });

  for (let level = 0; level <= max; level++) {

    const r = (R * level) / max;

    const text = svgElement("text", {

      x: cx + 7,

      y: cy - r + 3,

      "text-anchor": "start",

      class: "scale-label"

    });

    text.textContent = level;

    svg.appendChild(text);

  }

  const dataPts = config.axes.map((axis, i) => {

    const value = Math.max(0, Math.min(max, Number(axis.value) || 0));

    return point(i, (R * value) / max);

  });

  svg.appendChild(svgElement("polygon", {

    points: dataPts.map(([x, y]) => `${x.toFixed(2)},${y.toFixed(2)}`).join(" "),

    fill: "var(--fill)",

    stroke: "var(--stroke)",

    "stroke-width": 1.6,

    "stroke-linejoin": "round"

  }));

  dataPts.forEach(([x, y]) => {

    svg.appendChild(svgElement("circle", {

      cx: x.toFixed(2),

      cy: y.toFixed(2),

      r: 2.8,

      fill: "var(--dot)"

    }));

  });

  config.axes.forEach((axis, i) => {

    const [x, y] = point(i, R + 22);

    const ax = Math.cos(angle(i));

    let anchor = "middle";

    if (ax > 0.3) anchor = "start";

    else if (ax < -0.3) anchor = "end";

    const text = svgElement("text", {

      x: x.toFixed(2),

      y: (y + 3).toFixed(2),

      "text-anchor": anchor,

      class: "axis-label"

    });

    text.textContent = axis.label;

    svg.appendChild(text);

  });

}

function renderBars() {

  const list = document.getElementById("bar-list");

  list.replaceChildren();

  config.bars.forEach(bar => {

    const row = document.createElement("div");

    row.className = "bar-row";

    const segments = document.createElement("div");

    segments.className = "segments";

    for (let i = 0; i < bar.segments; i++) {

      const segment = document.createElement("span");

      segment.className = "seg" + (i < bar.filled ? " on" : "");

      segments.appendChild(segment);

    }

    const meta = document.createElement("div");

    meta.className = "bar-meta";

    meta.innerHTML = `

      <span class="xp">${bar.current} / ${bar.total}</span>

      <span class="dot-sep">●</span>

      <span class="lv">${bar.level}</span>

    `;

    row.append(segments, meta);

    list.appendChild(row);

  });

}

function renderEditor() {

  const list = document.getElementById("axis-editor-list");

  list.replaceChildren();

  config.axes.forEach((axis, index) => {

    const row = document.createElement("div");

    row.className = "axis-editor";

    const label = document.createElement("div");

    label.className = "axis-name";

    label.textContent = axis.label;

    const controls = document.createElement("div");

    controls.className = "score-control";

    const range = document.createElement("input");

    range.type = "range";

    range.min = "0";

    range.max = String(config.max);

    range.step = "0.5";

    range.value = String(axis.value);

    range.setAttribute("aria-label", axis.label);

    const number = document.createElement("input");

    number.className = "score-number";

    number.type = "number";

    number.min = "0";

    number.max = String(config.max);

    number.step = "0.5";

    number.value = String(axis.value);

    number.setAttribute("aria-label", `Valor de ${axis.label}`);

    const update = raw => {

      const value = Math.max(0, Math.min(config.max, Number(raw) || 0));

      config.axes[index].value = value;

      range.value = String(value);

      number.value = String(value);

      renderChart();

      saveConfig();

    };

    range.addEventListener("input", e => update(e.target.value));

    number.addEventListener("input", e => update(e.target.value));

    controls.append(range, number);

    row.append(label, controls);

    list.appendChild(row);

  });

}

function renderAll() {

  renderChart();

  renderBars();

  renderEditor();

}

document.getElementById("toggle-editor").addEventListener("click", () => {

  const editor = document.getElementById("editor");

  const button = document.getElementById("toggle-editor");

  const open = editor.classList.toggle("open");

  button.classList.toggle("active", open);

  button.setAttribute("aria-expanded", String(open));

});

document.getElementById("reset-button").addEventListener("click", () => {

  config = clone(DEFAULT_CONFIG);

  saveConfig();

  renderAll();

});

document.getElementById("export-button").addEventListener("click", async () => {

  const text = JSON.stringify(config, null, 2);

  const button = document.getElementById("export-button");

  try {

    await navigator.clipboard.writeText(text);

    button.textContent = "Copiado";

    setTimeout(() => button.textContent = "Copiar dados", 1000);

  } catch {

    button.textContent = "Não foi possível copiar";

    setTimeout(() => button.textContent = "Copiar dados", 1400);

  }

});

renderAll();

</script>

</body>

</html>

'''

out = Path("/mnt/data/life-radar-widget-notion-functional.html")

out.write_text(enhanced, encoding="utf-8")

print(f"Arquivo criado: {out}")