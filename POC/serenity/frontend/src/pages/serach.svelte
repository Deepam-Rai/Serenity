<script>

  let name=""
  let psd = ""
  async function postData() 
{
    const data = {'name':uname,
        'pswd':psd
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
<input bind:value={psd} type="password">
<br>
<button on:click={requestSender}>Login</button>

</div>
</div>


