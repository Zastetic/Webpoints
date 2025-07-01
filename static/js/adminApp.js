
// Cria a table padrão
const patern_table = document.getElementById("pontuation_table");
patern_table.remove();
const selectClass = document.getElementById("casa")

function setPeriodo(_periodo) {
  fetch('/set-periodo', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ periodo: _periodo })
  })
  .then(res => res.json())
  .then(data => {
    console.log("Sessão atualizada:", data);
  });
}

function restaurarSelecao() {
  const valorSalvo = parseInt(localStorage.getItem("atual_class") || "0");
  console.log(valorSalvo)

  // Espera até que o valor exista entre as opções
  selectClass.selectedIndex = valorSalvo
}

// Adiciona novas tabelas
function addTable(id, name, pontuation) {    
    const new_table = patern_table.cloneNode(true); //Copia ela

    new_table.id = id;
    new_table.getElementsByTagName("h3").name.textContent = name;
    new_table.getElementsByTagName("p").points.textContent = pontuation; //Muda suas propiedades em favor dos argumentos da função

    let parentElement = document.getElementById("holder");

    parentElement.appendChild(new_table);

    return 0;
}

// Adiciona as opções no campo de opções
function addOption(id, name) {
    const parentElement = document.getElementById("casa");
    let opt = document.createElement("option");

    opt.value = name;
    opt.id = id;
    opt.textContent = name;

    parentElement.appendChild(opt);
}

// PEGA O NOME DE TODAS AS CLASSES ALCOADAS NO DATABASE EM ORDENAÇÃO
function fetchClassesName() {
  return fetch(`/classes-name?periodo=${periodo}`)
    .then(res => {
      if (!res.ok) throw new Error(res.statusText);
      return res.json();
    })
    .then(data => data.names);
}

// PEGA OS PONTOS DE TODAS AS CLASSES NO DATABASE EM ORDENAÇÃO
function fetchClassesPontuation() {
  return fetch('/classes-points')
    .then(res => {
      if (!res.ok) throw new Error(res.statusText);
      return res.json();
    })
    .then(data => data.names);
}

// Faz todas as aquisições a API necessarias (nome e pontos de todas as salas)
fetchClassesName()
  .then(classesName => {
    const names = classesName
    fetchClassesPontuation()
      .then(classesPoints => {
        const points = classesPoints;

        for (var c = 0; c < names.length; c++) {
          addTable("pontuation_table_" + c, names[c], points[c]) //Cria uma mini table com cada informação das casas
          addOption(c, names[c])                                 //Coloca as opções com todos os nomes das casas
        }
        restaurarSelecao();
      })
      .catch(err => console.error(err));
  })
.catch(err => console.error(err));

// Modifica os pontos de determinada classe
function modify_points(event) {
    if (document.getElementById("casa").value == 0) { alert("Por favor, ensira uma casa."); return 0 }

    const clickedButton = event.submitter;
    let casa = document.getElementById("casa").value;
    let pontos = clickedButton.id

    window.location.href = `/modify_points?casa=${casa}&pontos=${pontos}`;
}

// FORM ACTIONS

// Adiciona os pontos para cada boa ação. Quantidade de pontos definida pelo ID.
const formGoodActions = document.getElementById('good-actions');
formGoodActions.addEventListener('submit', (event) => {event.preventDefault(); modify_points(event); localStorage.setItem("atual_class", selectClass.selectedIndex);});

// Remove os pontos pra cada ação negativa.
const formBadActions = document.getElementById('bad-actions');
formBadActions.addEventListener('submit', (event) => {event.preventDefault(); modify_points(event); localStorage.setItem("atual_class", selectClass.selectedIndex);});

// Seleção de periodo da turma.
const formPeriodo = document.getElementById("periodo");

formPeriodo.addEventListener('submit', (event) => {
    localStorage.setItem("atual_class", 0)
    const p = formPeriodo.childNodes[1].options[formPeriodo.childNodes[1].selectedIndex].id
    setPeriodo(p)
})  