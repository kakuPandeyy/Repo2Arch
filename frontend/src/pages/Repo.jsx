import React, { useState } from "react";

export default function Repo() {
  const [url, setUrl] = useState("");

  const handleSubmit = () => {
    console.log("Submitted URL:", url);
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-[#57C785] to-black">
      <div className="bg-slate-900/80  backdrop-blur-md rounded-2xl shadow-xl p-8 w-full max-w-md">
        <h1 className="text-2xl text-white  font-semibold b-4 text-center mb-10">
          Submit Repository URL
        </h1>

        <input
        type="text"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="Enter GitHub or project URL..."
          className="placeholder:text-gray-300   w-full h-18 p-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-purple-500 resize-none "
        />

        <button
          onClick={handleSubmit}
          className="mt-9 w-full  bg-gradient-to-r from-cyan-500 to-green-600 text-white py-3 rounded-xl font-medium hover:opacity-90 transition"
        >
          Submit
        </button>
      </div>
    </div>
  );
}
