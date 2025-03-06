import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [username, setUsername] = useState('');
  const [tweets, setTweets] = useState([]);

  const fetchTweets = async () => {
    try {
      const res = await axios.get(`http://127.0.0.1:5000/api/tweets?username=${username}`);
      setTweets(res.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h2>Twitter Analysis</h2>
      <input
        type="text"
        placeholder="Enter Twitter username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        style={{ marginRight: '10px' }}
      />
      <button onClick={fetchTweets}>Get Tweets</button>
      <ul>
        {tweets.map((tweet, index) => (
          <li key={index}>{tweet}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
