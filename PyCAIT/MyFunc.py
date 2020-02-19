'''
var response, status, i, header;
if (!proc.httpRequest) {
  proc.httpRequest = new XMLHttpRequest();
  proc.httpRequest.open(method, url, true);
  proc.httpRequest.send(data || null);
} else if (proc.httpRequest.readyState === 4) {
  response = proc.httpRequest.responseText;
  status = proc.httpRequest.status;
  proc.httpRequest = null;
  if (status === 200) {
    return response;
  } else {
    throw new Error(response);
  }
}
proc.pushContext('doYield');
proc.pushContext();
'''