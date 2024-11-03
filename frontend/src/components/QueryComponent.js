import React, { useState } from "react";
import axios from "axios";

function QueryComponent() {
    const [query, setQuery] = useState("");
    const [answer, setAnswer] = useState("");

    const handleQuery = async () => {
        try {
            const response = await axios.post("http://localhost:8000/query/", { query });
            setAnswer(response.data.answer);
        } catch (error) {
            console.error("Error querying document:", error);
            alert("Failed to query document. Please try again.");
        }
    };

    return (
        <div className="card">
            <h2>Query Document</h2>
            <input
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Enter your question"
            />
            <button onClick={handleQuery}>Query</button>
            {answer && <p className="answer">Answer: {answer}</p>}
        </div>
    );
}

export default QueryComponent;
