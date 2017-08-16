/**
 * Created by unsav on 16.08.17.
 */


 var sock = new SockJS('http://localhost:8001/echo');
 sock.onopen = function() {
     console.log('open');
     sock.send('test');
 };

 sock.onmessage = function(e) {
     console.log('message', e.data);
     sock.close();
 };

 sock.onclose = function() {
     console.log('close');
 };