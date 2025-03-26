window.addEventListener("load",initcontrols);
window.addEventListener("load",add);

function initcontrols()
{
	document.getElementById("txtUsername").textContent = ""; 
	document.getElementById("txtpassword").textContent = "";
	document.getElementById("txtUsername").focus();
}
function add()
{
	document.getElementById("btmsubmit").addEventListener("click",check);
}
function check()
{
	var username, pass; 
	username = document.getElementById("txtUsername").value; 
	pass = document.getElementById("txtpassword").value; 
	
	if(username == "" || pass == "")
	{
		alert("Information is missing");
		initcontrols();
	}
}