const cupcakesList = document.querySelector("#cupcakes-list");
const cupcakesForm = document.querySelector("#cupcakes-form")

async function get_cupcakes() {
    cupcakes = await axios.get("/api/cupcakes")
    for(let c of cupcakes.data.cupcakes) {
        const entry = document.createElement('li')
        
        // add the image
        const img = document.createElement('img')
        img.src = c.image
        img.height = 150
        entry.appendChild(img)
        
        // add the rest of the info
        const textSection = document.createElement('a') // using an anchor tag so we can link to an indvidual page later
        textSection.innerText = `Flavor: ${c.flavor}, Size: ${c.size}, Rating: ${c.rating}`
        entry.appendChild(textSection)
        
        cupcakesList.appendChild(entry)
    }
}

async function submit_cupcake(evt) {
    evt.preventDefault()
    
    // form fields
    const flavorField = cupcakesForm.querySelector("#flavor-field")
    const sizeField = cupcakesForm.querySelector("#size-field")
    const ratingField = cupcakesForm.querySelector("#rating-field")
    const imageField = cupcakesForm.querySelector("#image-field")
    
    const formData = {
        flavor: flavorField.value,
        size: sizeField.value,
        rating: ratingField.value,
        image: imageField.value,
    }
    
    newCupcake = await axios.post("/api/cupcakes", formData)
}

get_cupcakes();
cupcakesForm.querySelector("button").addEventListener("click", submit_cupcake)