function counter(){
	let contador = parseInt(document.getElementById('count').innerHTML);
    document.getElementById('count').innerHTML = contador + 1;
    console.log(contador);
    sendthang(contador);
}

function sendthang(contador){
    const csrftoken = Cookies.get('csrftoken');
    $.ajax({
        url: "http://127.0.0.1:8000/1/",
        type: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        data: {
            'score': contador,
        },
    })
}

function counter_add(){
    let contador = parseInt(document.getElementById('count').innerHTML);
    document.getElementById('count').innerHTML = contador + 1;
    sendthang(contador);
}

setInterval(counter, 1000);
