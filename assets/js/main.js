const nav=document.querySelector('.nav');const menu=document.querySelector('.menu');if(menu){menu.addEventListener('click',()=>nav.classList.toggle('open'));document.querySelectorAll('.nav-links a').forEach(a=>a.addEventListener('click',()=>nav.classList.remove('open')))}
document.getElementById('year')?.append(new Date().getFullYear());
