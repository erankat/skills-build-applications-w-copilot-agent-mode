import React, { useEffect, useState } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch('https://friendly-space-doodle-jq995746jg4cp49j-8000.app.github.dev/api/teams/')
      .then(response => response.json())
      .then(data => {
        console.log('Fetched teams:', data); // Log the fetched data for debugging
        setTeams(data);
      })
      .catch(error => console.error('Error fetching teams:', error));
  }, []);

  return (
    <div>
      <h1 className="display-4 text-center">Teams</h1>
      <ul className="list-group">
        {teams.map(team => (
          <li key={team.id} className="list-group-item">{team.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default Teams;
