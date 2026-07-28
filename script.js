async function loadLandfalls(){
    const tbody = document.getElementById("landfall-body"); 

    try{
        const response = await fetch("landfalls.json"); 
          if(!response.ok){
            throw new Error(`Failed to load information from landfalls.json (status ${response.status})`);
    }

    const landfalls = await response.json(); 

    //Render elements into HTML

    landfalls.forEach((event) => {
        const row = document.createElement("tr"); 

        const nameCell = document.createElement("td"); 
        nameCell.textContent = event.storm_name; 

        const dateCell = document.createElement("td"); 
        dateCell.textContent = event.date; 

        const windCell = document.createElement("td"); 
        windCell.textContent = event.max_wind; 

        row.appendChild(nameCell); 
        row.appendChild(dateCell); 
        row.appendChild(windCell); 
        tbody.appendChild(row); 
        }); 

    }  catch (error){

        console.error(error); 
        const row = document.createElement("tr");
        const cell = document.createElement("td");
        cell.colSpan = 3; //ensure error is readable to user 
        cell.textContent = "Could not load landfall data. Check if landfalls.json exists in this repository";
        row.appendChild(cell); 
        tbody.appendChild(row);
    }
}

loadLandfalls(); 

    
