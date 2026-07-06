const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('navLinks');

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navLinks.classList.toggle('active');
});

navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navLinks.classList.remove('active');
    });
});

document.addEventListener('click', (e) => {
    if (!navLinks.contains(e.target) && !hamburger.contains(e.target)) {
        hamburger.classList.remove('active');
        navLinks.classList.remove('active');
    }
});

window.addEventListener('scroll', () => {
    const navbar = document.getElementById('navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, observerOptions);

document.querySelectorAll('.section-title, .tech-item, .project-card, .about-text, .stat-box').forEach(el => {
    observer.observe(el);
});

const techItems = document.querySelectorAll('.tech-item');
techItems.forEach((item, index) => {
    item.style.transitionDelay = `${index * 0.05}s`;
});

const projectCards = document.querySelectorAll('.project-card');
projectCards.forEach((card, index) => {
    card.style.transitionDelay = `${index * 0.15}s`;
});

const authorPhotoBtn = document.getElementById('authorPhotoBtn');
const photoLightbox = document.getElementById('photoLightbox');
const lightboxClose = document.getElementById('lightboxClose');

if (authorPhotoBtn && photoLightbox) {
    authorPhotoBtn.addEventListener('click', () => {
        photoLightbox.classList.add('active');
    });

    const closeLightbox = () => photoLightbox.classList.remove('active');

    lightboxClose.addEventListener('click', closeLightbox);

    photoLightbox.addEventListener('click', (e) => {
        if (e.target === photoLightbox) closeLightbox();
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeLightbox();
    });
}