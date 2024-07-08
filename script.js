document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('juegoForm');
    const tableBody = document.getElementById('juegosTable').querySelector('tbody');
    let isUpdating = false;

    //async permite que la función se comporte de manera asíncrona, 
    //puede ejecutar operaciones sin bloquear el hilo principal de ejecucion

    const fetchJuegos = async () => {
        //luego cambiaremos la url por https://<hostdepanywhere>/productos
        const response = await fetch('https://nehuborrajo.pythonanywhere.com/juegos');// promesa: esperar a que se complete la solicitud HTTP
        const juegos = await response.json(); //esperar a que se complete la conversión de la respuesta a JSON
        tableBody.innerHTML = '';
        juegos.forEach(juego => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${juego.id}</td>
                <td>${juego.nombre}</td>
                <td>${juego.version}</td>
                <td>${juego.precio}</td>
                <td>
                    <button onclick="editJuego(${juego.id}, '${juego.nombre}', '${juego.version}', ${juego.precio})">Editar</button>
                    <button onclick="deleteJuego(${juego.id})">Eliminar</button>
                </td>
            `;
            tableBody.appendChild(row);
        });
    };

    const addJuego = async (juego) => {
        await fetch('https://nehuborrajo.pythonanywhere.com/agregar_juego', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(juego)
        });
        fetchJuegos();
    };

    const updateJuego = async (id, juego) => {
        await fetch(`https://nehuborrajo.pythonanywhere.com/actualizar_juego/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(juego)
        });
        fetchJuegos();
    };

    const deleteJuego = async (id) => {
        await fetch(`https://nehuborrajo.pythonanywhere.com/eliminar_juego/${id}`, {
            method: 'DELETE'
        });
        fetchJuegos();
    };

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const id = document.getElementById('juegoId').value;
        const nombre = document.getElementById('nombre').value;
        const version = document.getElementById('version').value;
        const precio = document.getElementById('precio').value;
        const juego = { nombre, version, precio };

        if (isUpdating) {
            updateJuego(id, juego);
            isUpdating = false;
        } else {
            addJuego(juego);
        }

        form.reset();
        document.getElementById('juegoId').value = '';
    });

    window.editJuego = (id, nombre, version, precio) => {
        document.getElementById('juegoId').value = id;
        document.getElementById('nombre').value = nombre;
        document.getElementById('version').value = version;
        document.getElementById('precio').value = precio;
        isUpdating = true;
    };

    window.deleteJuego = (id) => {
        if (confirm('¿Estás seguro de eliminar este juego?')) {
            deleteJuego(id);
        }
    };

    fetchJuegos();
});
