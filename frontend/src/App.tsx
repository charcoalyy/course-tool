import Dashboard from "@pages/Dashboard";
import Home from "@pages/Home";
import NotFound from "@pages/NotFound";
import Profiling from "@templates/Profiling";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/profiling" element={<Profiling />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </Router>
  );
};

export default App;
