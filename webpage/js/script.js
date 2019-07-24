const Http = new XMLHttpRequest();
const url='https://raspberrypi-lia:7772/full-demo';

function runFullDemo() {
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange = (e) => {
      console.log(Http.responseText)
    }
}