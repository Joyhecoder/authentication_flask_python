function delete_note(noteId){
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({noteId}),
    }).then((res) => {
        window.location.href= "/"
    })
}