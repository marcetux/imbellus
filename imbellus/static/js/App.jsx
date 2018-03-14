import React from "react";
import ImbellusNavigator from "./ImbellusNavigator";
import { PageHeader } from "react-bootstrap";

require('../css/imbellus.css');
var $ = require('jquery');

export default class App extends React.Component {
    constructor(props) {
        super(props);
    }

    render () {
        return (
            <PageHeader>
                <div className='header-contents'>
                <ImbellusNavigator name='An Imbellus Component!' />
                </div>
            </PageHeader>
        );
    }
}