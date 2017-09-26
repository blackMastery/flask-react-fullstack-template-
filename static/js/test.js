var $ = require('jquery')

getPythonHello(){
    $.get(window.location.href + 'hello', (data)=>{
        console.log(data);
        this.personliseGreeting(data);
    });
}