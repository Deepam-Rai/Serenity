<script>
    let outpu = ""
async function postData() 
{
    const uname = document.getElementById("uname").valu
    const psw = document.getElementById("psw")
    alert(psw)
    const data = {'name':uname,
        'pswd':psw
    }
    alert("Sad")
    console.log(data)
    const response = await fetch("http://localhost:9512/login", {
    method: 'POST', 
    mode: 'cors', 
    cache: 'no-cache', 
    credentials: 'same-origin',
    headers: {'Content-Type': 'application/json'},
    redirect: 'follow',
    referrerPolicy: 'no-referrer',
    body: JSON.stringify(data) 
  });
  return response.json();
}
    function requestSender()
    {
        postData().then((data)=>{alert(data['output'])})
        
    }
</script>
<style>
form {border: 3px solid #f1f1f1;
    width: 50%;
    position: absolute;
    top:250px;
    margin-left:25%;
}

input[type=text], input[type=password] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

button {
  background-color: #04AA6D;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
}

button:hover {
  opacity: 0.8;
}

.cancelbtn {
  width: auto;
  padding: 10px 18px;
  background-color: #f44336;
}

.imgcontainer {
  text-align: center;
  margin: 24px 0 12px 0;
}

img.avatar {
  width: 40%;
  border-radius: 50%;
}

.container {
  padding: 16px;
}

span.psw {
  float: right;
  padding-top: 16px;
}

/* Change styles for span and cancel button on extra small screens */
@media screen and (max-width: 300px) {
  span.psw {
     display: block;
     float: none;
  }
  .cancelbtn {
     width: 100%;
  }
}
</style>

<form >
    <h2 style="text-align: center">Login Form</h2>
  <div class="imgcontainer">
  </div>

  <div class="container">
    <label for="uname"><b>Username</b></label>
    <input type="text" placeholder="Enter Username" id="uname" required>

    <label for="psw"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" id="psw" required>
        
    <button on:click={requestSender}>Login</button>
    </div>

</form>
