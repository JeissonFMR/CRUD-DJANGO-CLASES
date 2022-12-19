// let responsables = [];

// const listarResponsables = async (idPrograma) => {
//     try {
//         const response = await fetch(`/get_responsable/${idPrograma}`);
//         const data = await response.json();

//         if (data.message === "Success") {
//             responsables = data.responsables;
//             let opciones = ``;
//             responsables.forEach((responsable) => {
//                 opciones += `<option value='${responsable.id}'>${responsable.nombre}</option>`;
//             });
//             coCiudad.innerHTML = opciones;
            
//         } else {
//             alert("Países no encontrados...");
//         }
//     } catch (error) {
//         console.log(error);
//     }
// };

// const listarProgramas = async () => {
//     try {
//         const response = await fetch("/get_programa");
//         const data = await response.json();

//         if (data.message === "Success") {
//             let opciones = ``;
//             data.programas.forEach((programa) => {
//                 opciones += `<option value='${programa.id}'>${programa.nombre_programa}</option>`;
//             });
//             coPais.innerHTML = opciones;
//             listarResponsables(data.programas[0].id);
//         } else {
//             alert("Países no encontrados...");
//         }
//     } catch (error) {
//         console.log(error);
//     }
// };

// const cargaInicial = async () => {
//     await listarProgramas();

//     coPais.addEventListener("change", (event) => {
//         listarResponsables(event.target.value);
//     });

// };

// window.addEventListener("load", async () => {
//     await cargaInicial();
// });