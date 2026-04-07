
import { useState } from 'react'

function Budy() {
    const [message,setMessage] = useState("");
    const [chat,setChat] = useState([]);
    const sendmessage = async ()=> {
        if (!message) return;
        const res = await fetch ("http://127.0.0.1:5000/api/chat",{
            method:"POST",
            headers:{
                "content-type":"application/json"
            },
            body: JSON.stringify({message}),
        });

        const data = await res.json();
        setChat([...chat, {user:message, bot: data.reply}]);
        setMessage("");
    }


  return (
    <div class='main'>
        <h2 class = 'chat'>Chatbot</h2>

        <div>
            {chat.map((mesaj,index) =>(
             <div   key={index}>
                <p><b>I:</b>{mesaj.user}</p>
                <p><b>Bot:</b>{mesaj.bot}</p>
             </div>  
            ))}
        </div>
        <input className='text-red-800'
            value={message}
            onChange={(e)=> setMessage(e.target.value)}
            placeholder='ask something !'        
        />
          <button onClick={sendmessage}> send </button>



    </div>
  )
}



export default Budy
