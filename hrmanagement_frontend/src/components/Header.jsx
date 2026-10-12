import {  Link} from "react-router-dom"
import './header.css'
function Header(){
  return(
    <div className="header">
        <Link to="/">Home</Link>
         <Link to="/About">About</Link>
          <Link to="/Contact">contact</Link>
    </div>
  )
}
export default Header