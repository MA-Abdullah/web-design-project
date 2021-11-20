function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

$(".nav .nav-link").on("click", function(){
  $(".nav").find(".active").removeClass("active");
  $(this).addClass("active");
});
