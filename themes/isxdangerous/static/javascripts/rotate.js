window.addEventListener('DOMContentLoaded', (event) => {
  var rotatorWait = window.setInterval(rotate, 2000);
});

function rotate() {
  var rotator = document.getElementById('rotate');

  switch (rotator.innerHTML) {
    case 'X':
      rotator.innerHTML = 'Y';
      break;
    case 'Y':
      rotator.innerHTML = 'Z';
      break;
    case 'Z':
      rotator.innerHTML = 'Q';
      break;
    case 'Q':
      rotator.innerHTML = 'M';
      break;
    case 'M':
      rotator.innerHTML = 'X';
      break;
  };
};
