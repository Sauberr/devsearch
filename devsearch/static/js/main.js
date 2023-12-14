

    // GET SEARCH FORM AND PAGE LINKS
    let searchform = document.getElementById('searchform')
    let pagelinks = document.getElementsByClassName('page-link')
    // ENSURE SEARCH FORM EXIST
    if(searchform){
        for(let i=0; pagelinks.length > i; i++ ){
            pagelinks[i].addEventListener('click', function (e) {
                e.preventDefault()

                // GET THE DATA ATTRIBUTE
                let page = this.dataset.page
                // ADD HIDDEN SEARCH INPUT TO FORM
                searchform.innerHTML += `<input value=${page} name="page" hidden/>`
                // SUBMIT FORM
                searchform.submit()
            })
        }
    }


    let tags =  document.getElementsByClassName('project-tag')

    for (let i=0; tags.length > i; i++){
        tags[i].addEventListener('click', (e) => {
            let tagId = e.target.dataset.tag
            let projectId = e.target.dataset.project

            fetch('http://127.0.0.1:8000/api/remove-tag/', {
                method:'DELETE',
                headers:{
                    'Content-Type': 'applications/json'
                },
                body:JSON.stringify({'project': projectId, 'tag': tagId})
            })
                .then(response => response.json())
                .then(data => {
                    e.target.remove()
                })
        })
    }
