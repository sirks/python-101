const URL = 'http://localhost:5000'
const table = document.getElementById("list-body");
const nameEl = document.getElementById("hero-name");
const powerEl = document.getElementById("hero-power");


async function save_line() {
    name = nameEl.value
    power = powerEl.value
    data = [name, power]
    const response = await fetch(`${URL}/superheroes`, { method: 'POST', body: JSON.stringify(data) });
    const idx = await response.json()
    debugger;
    add_line(idx, name, power)
}

function add_line(idx, name, power) {
    const row = table.insertRow(0);
    let cell = row.insertCell(0)
    cell.innerHTML = 'X';
    cell.onclick = () => remove_row(row, idx);
    row.insertCell(1).innerHTML = idx;
    row.insertCell(2).innerHTML = name;
    row.insertCell(3).innerHTML = power;
}

async function remove_row(row, db_idx) {
    await fetch(`${URL}/superheroes/${db_idx}`, { method: 'DELETE' })
    table.removeChild(row)
}

async function get_all() {
    const response = await fetch(`${URL}/superheroes`)
    const heroes = await response.json()
    heroes.forEach(el => add_line(el[0], el[1], el[2]));
}



get_all();