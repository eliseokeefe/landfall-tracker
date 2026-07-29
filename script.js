function formatDate(yyyymmdd){
    //create separate variables for year, month, day
    const year = yyyymmdd.slice(0,4); 
    const month = yyyymmdd.slice(4,6); 
    const day = yyyymmdd.slice(6,8);
    return month + "/" + day + "/" + year; 
}

async function loadLandfalls(){
    //utilizing the id in my HTML, I define a constant to work with this later in my JS code 
    const tbody = document.getElementById("landfall-body"); 
    //using a try catch statement to load the information in order to ensure errors are expressed to the user 
    try{
          const response = await fetch("/api/landfalls");
          if(!response.ok){ //if the json cannot be loaded, display the error to the user 
            throw new Error(`Failed to load information from landfalls.json (status ${response.status})`);
          }

    const landfalls = await response.json(); 

    //Render each element into HTML displaying storm name, date, and max wind speed  

    landfalls.forEach((event) => {
        const row = document.createElement("tr"); //make each landfall a seperate row in HTML

        const nameCell = document.createElement("td"); //display the storm's name
        nameCell.textContent = event.storm_name; 

        const dateCell = document.createElement("td");  //display the storm's date
        dateCell.textContent = formatDate(event.date); 

        const windCell = document.createElement("td");   //display the landfall's max wind speed
        windCell.textContent = event.max_wind; 

        //Add name, date, and max wind speed to HTML code as well as create the row itself 
        row.appendChild(nameCell); 
        row.appendChild(dateCell); 
        row.appendChild(windCell); 
        tbody.appendChild(row); 
        }); 

    }  catch (error){

        console.error(error); 
        const row = document.createElement("tr");
        const cell = document.createElement("td"); //create cell to display error 
        cell.colSpan = 3; //ensure error is readable to user 
        cell.textContent = "Could not load landfall data. Check if landfalls.json exists in this repository";
        row.appendChild(cell); 
        tbody.appendChild(row);
    }
}

// Call function to actually load in landfalls to browser 
loadLandfalls(); 

    
