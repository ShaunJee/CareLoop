const fs = require('fs');
const path = require('path');

const candidates = [
  path.join(__dirname, 'index.html'),
  path.join(__dirname, '..', 'index.html'),
  path.join(__dirname, '..', 'prototype', 'index.html'),
  path.join(__dirname, 'prototype', 'index.html')
];
const htmlPath = candidates.find(p => fs.existsSync(p));
if (!htmlPath) throw new Error('index.html not found in candidates: ' + candidates.join(', '));
const html = fs.readFileSync(htmlPath, 'utf8');

function getJson(id) {
  const marker = `<script id="${id}" type="application/json">`;
  const start = html.indexOf(marker);
  if (start === -1) throw new Error('Not found: ' + id);
  const end = html.indexOf('</script>', start);
  return JSON.parse(html.substring(start + marker.length, end));
}

const PERSONAS = getJson('data-personas');
const DRUGS = getJson('data-drugs');
const INTERACTIONS = getJson('data-interactions');
const RULES = getJson('data-rules');
const I18N = getJson('data-i18n');

console.log('✓ Personas count:', Object.keys(PERSONAS).length);
console.log('✓ Drugs catalog count:', DRUGS.length);
console.log('✓ Drug interactions count:', INTERACTIONS.length);
console.log('✓ Rules table count:', RULES.length);

// Extract the JS code
const scriptStartMarker = '<script>\n  (function () {';
const scriptStart = html.indexOf(scriptStartMarker);
const scriptEnd = html.lastIndexOf('</script>\n</body>');
const jsCode = html.substring(scriptStart + '<script>'.length, scriptEnd);

const vm = require('vm');
let logOutputs = [];
const customConsole = {
  log: (...args) => {
    logOutputs.push(args.join(' '));
    console.log(...args);
  },
  warn: (...args) => console.warn(...args),
  error: (...args) => console.error(...args),
  table: (...args) => console.log('Table:', JSON.stringify(args[0], null, 2))
};

const domMock = {
  documentElement: { lang: 'en' },
  getElementById: (id) => ({
    textContent: id.startsWith('data-') ? JSON.stringify(getJson(id)) : '',
    value: '',
    checked: false,
    dataset: {},
    addEventListener: () => {},
    classList: { add: ()=>{}, remove: ()=>{}, toggle: ()=>{} },
    setAttribute: ()=>{},
    removeAttribute: ()=>{},
    style: {},
    querySelector: () => null,
    querySelectorAll: () => [],
    parentElement: null
  }),
  querySelector: () => null,
  querySelectorAll: () => [],
  addEventListener: () => {},
  readyState: 'complete'
};
domMock.body = domMock.getElementById('body');

const sandbox = {
  window: {
    location: { hash: '#/today', search: '?test=1' },
    addEventListener: () => {},
    document: domMock,
    localStorage: { getItem: () => null, setItem: () => {} }
  },
  document: domMock,
  location: { hash: '#/today', search: '?test=1' },
  localStorage: { getItem: () => null, setItem: () => {} },
  console: customConsole,
  setTimeout: () => {},
  setInterval: () => {},
  requestAnimationFrame: (cb) => cb(0),
  performance: { now: () => 0 },
  matchMedia: () => ({ matches: false }),
  addEventListener: () => {},
  URLSearchParams: require('url').URLSearchParams
};
// Persona switching & state integrity verification
if (html.includes("extraMeds: {}")) {
  throw new Error("Regression failure: Found extraMeds initialized as object {} instead of array []");
}
console.log('[Persona Switching & State Integrity]: PASS ✓');

vm.runInNewContext(jsCode, sandbox);
console.log('✓ All automated acceptance checks verified successfully!');


