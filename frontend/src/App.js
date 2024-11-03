import React from "react";
import UploadForm from "./components/UploadForm";
import QueryComponent from "./components/QueryComponent";
import "./App.css"; // Import the CSS file

function App() {
    return (
        <div className="app-container">
            <header className="app-header">
                <h1>DOCZY</h1>
                <h3>A Document Management Inventory</h3>
                <p className="app-description">
                    Effortlessly manage, upload, and retrieve documents with ease. DOCZY provides secure storage and smart search capabilities for all your documents.
                </p>
            </header>
            <div className="content-container">
                <UploadForm />
                <QueryComponent />
            </div>
        </div>
    );
}

export default App;
