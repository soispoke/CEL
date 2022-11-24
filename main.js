import {PythonShell} from 'python-shell';

alert("This alert box was called with the onload event");


var pyshell = new PythonShell('main.py');

const blockchain = "bnb";
const address = "0x0d8ce2a99bb6e3b7db580ed848240e4a0f9ae153";
const start_date = "2022-09-24 00:00:00";
const end_date = "2022-10-01 00:00:00";

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