document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('busca');
    const teamList = document.getElementById('lista-equipes');
    const teams = Array.from(teamList.getElementsByTagName('article'));

    searchInput.addEventListener('input', function() {
        const query = searchInput.value.toLowerCase();
        let found = false;
        teams.forEach(function(team) {
            const teamName = team.querySelector('h3').textContent.toLowerCase();
            if (teamName.includes(query)) {
                team.style.display = '';
                found = true;
            } else {
                team.style.display = 'none';
            }
        });

        const noResultMessage = document.getElementById('sem-resultado');
        noResultMessage.hidden = found;
    });
})