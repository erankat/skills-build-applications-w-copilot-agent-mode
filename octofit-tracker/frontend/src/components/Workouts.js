import React, { useEffect, useState } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch('https://friendly-space-doodle-jq995746jg4cp49j-8000.app.github.dev/api/workouts/')
      .then(response => response.json())
      .then(data => {
        console.log('Fetched workouts:', data); // Log the fetched data for debugging
        setWorkouts(data);
      })
      .catch(error => console.error('Error fetching workouts:', error));
  }, []);

  return (
    <div>
      <h1 className="display-4 text-center">Workouts</h1>
      <div className="row">
        {workouts.map(workout => (
          <div key={workout.id} className="col-md-4">
            <div className="card mb-4">
              <div className="card-body">
                <h5 className="card-title">{workout.name}</h5>
                <p className="card-text">{workout.description}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Workouts;
