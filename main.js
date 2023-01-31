import {PythonShell} from 'python-shell';

alert("This alert box was called with the onload event");


var pyshell = new PythonShell('main.py');

const blockchain = "bnb";
const address = "0x1f9840a85d5af5bf1d1762f925bdaddc4201f984";
const start_date = "2023-01-23 00:00:00";
const end_date = "2023-01-27 00:00:00";

pyshell.send(JSON.stringify([
    blockchain,
    address,
    start_date,
    end_date]));

pyshell.on('message', function (message) {
    // received a message sent from the Python script (a simple "print" statement)
    console.log(message);
});

// end the input stream and allow the process to exit
pyshell.end(function (err) {
    if (err){
        throw err;
    };

    console.log('finished');
});;
