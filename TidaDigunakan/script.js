const heading = document.getElementById("title")
const paragraph = document.querySelectorAll(".paragraph")
const button = document.getElementById("change")
const container = document.querySelector(".container")

heading.textContent = "Pembelajaran JS"
paragraph.forEach((p, index) => {
    p.innerHTML = `paragraf ke ${index + 1}`
});

button.addEventListener("click", function(){
    alert("ini alert");
    document.writeln("<p style='color:red; text-align:center;'>Ini document writeln</p>")
    console.log("ini console log")
    heading.style.color = "#ff4b5c";
    heading.textContent = "Ini Mode Gelap";
    container.classList.toggle("dark-mode");
})