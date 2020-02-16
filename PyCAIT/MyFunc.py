var response = '123', i, header;
function myFun() {
  if(proc.httpRequest.readyState == 4 && proc.httpRequest.status == 200){    
    response = proc.httpRequest.responseText;
    //console.log(proc.httpRequest);
    console.log(response);
    return response
  }
}
if (!proc.httpRequest) {
  proc.httpRequest = new XMLHttpRequest();
  proc.httpRequest.onreadystatechange = myFun; 
  proc.httpRequest.open(method, url, true);
  proc.httpRequest.send(data || null);
}
proc.pushContext('doYield');
proc.pushContext();
console.log(proc.httpRequest);
return response;