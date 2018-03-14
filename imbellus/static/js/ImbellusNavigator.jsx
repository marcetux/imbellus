import React from "react";
import { Button, Grid, Row, Col } from "react-bootstrap";

var $ = require('jquery');

export default class ImbellusNavigator extends React.Component {
    constructor(props) {
        super(props);
        this.state = {history: []}; //maybe add a history feature...
        this.getAbout = this.getAbout.bind(this);
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({value: event.target.value});
    }
    
    handleSubmit(event) {
        alert('A name was submitted: ' + this.state.value);
        event.preventDefault();
    }
    
    getAbout() {
        $.get(window.location.href + 'about', (data) => {  
            console.log(data);
          });
    }


    testGeocode() {
       
    }


    testReverseGeocode() {
        $.get(window.location.href + 'about', (data) => {  
            console.log(data);
          });
       
    }


    testGeometricDistance() {
       
    }

    render () {
        return (
            <Row>
            <Button bsSize="large"  onClick={this.getAbout}> Distance
            </Button>
            <Button bsSize="large"  onClick={this.testReverseGeocode}>Reverse
            </Button>
            </Row>
        );
    }
}