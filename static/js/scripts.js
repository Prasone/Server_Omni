function showModal(url, name) {
    var modal = document.getElementById('cameraModal');
    var modalImage = document.getElementById('modalImage');
    var modalTitle = document.getElementById('modalTitle');

    modalImage.src = url;
    modalTitle.innerText = name + ' Camera View';
    modal.style.display = "block";
}

function closeModal() {
    var modal = document.getElementById('cameraModal');
    modal.style.display = "none";
}

window.onclick = function(event) {
    var modal = document.getElementById('cameraModal');
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
