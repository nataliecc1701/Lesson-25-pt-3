const cupcakesList = document.querySelector("#cupcakes-list");
const cupcakesForm = document.querySelector("#cupcakes-form");

// form fields
const flavorField = cupcakesForm.querySelector("#flavor-field")
const sizeField = cupcakesForm.querySelector("#size-field")
const ratingField = cupcakesForm.querySelector("#rating-field")
const imageField = cupcakesForm.querySelector("#image-field")

function displayCupcake(cupcake) {
    const entry = document.createElement('li')
        
    // add the image
    const img = document.createElement('img')
    img.src = cupcake.image
    img.height = 150
    entry.appendChild(img)
    
    // add the rest of the info
    const textSection = document.createElement('a') // using an anchor tag so we can link to an indvidual page later
    textSection.innerText = `Flavor: ${cupcake.flavor}, Size: ${cupcake.size}, Rating: ${cupcake.rating}`
    entry.appendChild(textSection)
    
    cupcakesList.appendChild(entry)
}

async function get_cupcakes() {
    cupcakes = await axios.get("/api/cupcakes")
    for(let c of cupcakes.data.cupcakes) {
        displayCupcake(c)
    }
}

async function submit_cupcake(evt) {
    evt.preventDefault()
    
    const formData = {
        flavor: flavorField.value,
        size: sizeField.value,
        rating: ratingField.value,
    }
    if (imageField.value) {
        formData.image = imageField.value
    }
    
    console.log(formData.image)
    
    try {
        newCupcake = await axios.post("/api/cupcakes", formData)
        displayCupcake(newCupcake.data.cupcake)
    }
    catch {
        alert("Cupcake post failed")
    }
}

get_cupcakes();
cupcakesForm.querySelector("button").addEventListener("click", submit_cupcake)