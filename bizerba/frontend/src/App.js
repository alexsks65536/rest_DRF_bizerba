import React from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';
import CustomerList from './components/Customer.js';

class App extends React.Component {
   constructor(props) {
       super(props)
       this.state = {
           'customers': []
       }
   }

componentDidMount() {
   axios.get('http://127.0.0.1:8000/api/v1/customer/')
       .then(response => {
           const customers = response.data
               this.setState(
               {
                   'customers': customers
               }
           )
       }).catch(error => console.log(error))
}


   render () {
       return (
           <div>
               <CustomerList customers={this.state.customers} />
           </div>
       )
   }
}


export default App;
