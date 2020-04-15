// ---------- websocket ---------- //
var ws = new WebSocket('ws://localhost:8765');

ws.onopen = () => console.log('Connection opened!');
ws.onmessage = event => console.log('Received: ', event.data);
ws.onclose = () => console.log('Connection closed!');

ws.send('Hello!');
ws.close();

// ------------ http ------------- //
fetch('http://localhost:7654')
    .then(res => res.text())
    .then(res => console.log(res));
fetch('http://localhost:7654', {method: 'POST', body: 'test'})
    .then(res => res.text())
    .then(res => console.log(res));