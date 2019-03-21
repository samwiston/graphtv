/*function loadFile(filePath) {
    var result = null;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", filePath, false);
    xmlhttp.send();
    if (xmlhttp.status==200) {
      result = xmlhttp.responseText;
    }
    return result;
  }

loadFile("https://github.com/samwiston/graphtv/blob/master/testFile.json")*/

var requestURL = 'https://github.com/samwiston/graphtv/blob/master/testFile.json';
var request = new XMLHttpRequest();
request.open('GET', requestURL);

request.responseType = 'json';
request.send();

request.onload = function() {
    var superHeroes = request.response;
    console.log(superHeroes);
  }