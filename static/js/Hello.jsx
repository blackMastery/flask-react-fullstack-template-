import React from 'react'
var $ = require('jquery')

export default class Hello extends React.Component{
    constructor(props){
        super(props)
        this.state ={
            greeting: 'Helloooo ' + this.props.name
        }

        this.getPythonHello = this.getPythonHello.bind(this)
        this.personliseGreeting = this.personliseGreeting.bind(this)

    }



    getPythonHello(){
    $.get(window.location.href + 'hello', (data)=>{
        console.log(data);
        this.personliseGreeting(data);
    });
}
    personliseGreeting(greeting){
        this.setState({greeting:greeting+ ' '+ this.props.name+ '!'});

    }


    render(){
        return(
            <div>
                <h1>{this.state.greeting}</h1>
                <hr/>
                <button onClick={this.getPythonHello}>
                    Say Hello
                </button>

                </div>

        )
    }

}