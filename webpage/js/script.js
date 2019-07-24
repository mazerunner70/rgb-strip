const Http = new XMLHttpRequest();
const url='http://raspberrypi-lia:2280/full-demo';

function runFullDemo() {
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange = (e) => {
      console.log(Http.responseText)
    }
}