import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Repo from './pages/Repo';
import FolderArch from './pages/FolderArch';

import './App.css';

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          
          <Route path="/repo" element={<Repo />} />
          <Route path="/folderArch" element={<FolderArch />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;