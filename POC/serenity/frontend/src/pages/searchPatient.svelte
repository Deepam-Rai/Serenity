<script>

    let name=""
    let psd = ""
    async function postData() 
  {
      const data = {'name':name
      }
      alert("Sad")
      console.log(data)
      const response = await fetch("http://localhost:9512/search", {
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
    .container {
    padding: 16px;
  }
  </style>
  <div >
    <h2 style="text-align: center">Search </h2>
  <div class="imgcontainer">
  </div>
  
  <div class="container">
  
  <input bind:value={name}>
  <br>
  <br>
  <button on:click={requestSender}>Login</button>
  
  </div>
  </div>
  
  
  