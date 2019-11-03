window.addEventListener('DOMContentLoaded', (event) => {
  document.getElementById('mobile-nav-button').addEventListener('click', toggle);
  document.getElementById('mobile-nav-bg').addEventListener('click', toggle);
});

function toggle() {
  console.log('toggled');
  document.getElementById('mobile-nav-wrap').classList.toggle('hidden');
  document.getElementById('mobile-nav-bg').classList.toggle('hidden');
  document.getElementById('ham-icon').classList.toggle('hidden');
  document.getElementById('x-icon').classList.toggle('hidden');
};
