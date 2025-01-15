document.addEventListener("DOMContentLoaded", () => {

//variables
let btn = document.getElementById("btn")

let result_container = document.getElementById("resultContainer")
let select_btn = document.getElementById("select")

//display_function
function display_result(prediction) {
    const resultContainer = document.getElementById("resultContainer");
    const resultText = document.getElementById("resultText");
    resultText.textContent = `The image is classified as: ${prediction}`;
    resultContainer.classList.remove("d-none"); // Show the result container
}

//handling select
async function handle_option(value){
    value = "/" + value

    
    let form_data = new FormData();
    let file = document.getElementById("imageUpload").files[0]
    form_data.append("img_file", file)

    let response = await fetch(value, {
        method: "POST",
        body: form_data
    })

    let data = await response.json()

    display_result(data.prediction)
}

btn.addEventListener("click", (e) => {
    e.preventDefault()
    let option_val = select_btn.value
    handle_option(option_val)
})

})