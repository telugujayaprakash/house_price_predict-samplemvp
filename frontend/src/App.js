import React, { useState } from "react";

function App() {
  const [features, setFeatures] = useState({ rooms: 3, size: 1500, age: 10 });
  const [prediction, setPrediction] = useState(null);

  const handleChange = (e) => {
    setFeatures({ ...features, [e.target.name]: e.target.value });
  };

  const handlePredict = async () => {
    const response = await fetch("https://samplemvp.onrender.com/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ features: [features.rooms, features.size, features.age] }),
    });
    const data = await response.json();
    setPrediction(data.prediction);
  };

  return (
    <div>
      <h1>House Price Predictor</h1>
      <input name="rooms" placeholder="Rooms" onChange={handleChange} />
      <input name="size" placeholder="Size (sq ft)" onChange={handleChange} />
      <input name="age" placeholder="Age of house" onChange={handleChange} />
      <button onClick={handlePredict}>Predict</button>
      {prediction && <h2>Predicted Price: ${prediction}</h2>}
    </div>
  );
}

export default App;
