// guardo en lis un arrays con todos los li
let lis = document.querySelectorAll('.seeLi');
// en una variable en h1 que contiene la cantidad de libros
let h1Cant = document.querySelector("#cantLibros")

// al documento le agrego un event listener que se activa cuando termina de cargar el dom
// mediante una funcion flecha hago una serie de cosas
document.addEventListener("DOMContentLoaded", () => {
    // primero al inner de mi h1Cant le agrego la cantidad de objetos que tiene mi lis array, que es igual a la cantidad de libros
    h1Cant.innerHTML = h1Cant.innerHTML + lis.length;
    // luego defino una funcion flecha para cada elemento de lis
    // donde le pido un parametro li
    lis.forEach(liI => {
        // del cual extraigo su data-number y se lo agrego al lado de su inner
        liI.innerHTML = `${liI.dataset.number}. ` + liI.innerHTML ; 
    })
});

// defino una variable search que contiene el elemento input #searchBar
let search = document.querySelector("#searchBar")

// le digo que cuando el usuario deje de escribir
search.onkeyup = () => {
    // para cada elemento li en lis
    lis.forEach(li => {
        // con (li.innerHTML.slice(2, li.innerHTML.length -1)) le estoy diciendo que me parta el string desde su tercer caracter hasta su último caracter =>
        // porque sino a la hora de buscar algun libro que tiene números me salidrian lo que contienen ese numero en su index que es el data-number =>
        // ya que lo sume al innerHTML original del li cuando cargue la pág;

        // si su inner no contiene el valor de mi busqueda
        if(!li.innerHTML.slice(2, li.innerHTML.length -1).includes(search.value)){
            // lo oculta
            li.hidden = true;
        }
        else {
            // en el caso contrario lo muestra
            li.hidden = false;
        }
    })
}
