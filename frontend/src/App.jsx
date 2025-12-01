import React, { useState } from "react";
import axios from "axios";
import "./App.css";

const API_BASE = "http://localhost:5000";

export default function App() {
  const [title, setTitle] = useState("");
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handlePredict = async () => {
    if (!title && !text) return;

    setLoading(true);
    const res = await axios.post(`${API_BASE}/api/predict`, { title, text });
    setResult(res.data);
    setLoading(false);
  };

  return (
    <div className="app-container">
      <div className="glass-card">

        <h1 className="title">Fake News Classifier</h1>

        <div className="input-group">
          <label>Headline</label>
          <input
            type="text"
            placeholder="Enter news headline"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
        </div>

        <div className="input-group">
          <label>Body</label>
          <textarea
            placeholder="Enter news content"
            value={text}
            onChange={(e) => setText(e.target.value)}
            rows="5"
          ></textarea>
        </div>

        <button className="predict-btn" onClick={handlePredict}>
          {loading ? "Analyzing..." : "Check News"}
        </button>

        {result && (
          <div className="result-box">
            <h2 className={result.prediction === "FAKE" ? "fake" : "real"}>
              {result.prediction}
            </h2>
            <p className="confidence">
              Confidence: {(result.confidence * 100).toFixed(2)}%
            </p>
          </div>
        )}
      </div>
    </div>
  );
}
