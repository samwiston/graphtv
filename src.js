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

$.getJSON('https://samwiston.github.io/graphtv/testFile.json', function(data) {
    document.getElementById("title").innerHTML = data.tt0087305.primaryTitle
    console.log(data)
});