// Mobile Navigation Toggle
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

hamburger.addEventListener('click', () => {
    navMenu.classList.toggle('active');
    hamburger.classList.toggle('active');
});

// Close mobile menu when clicking on a link
document.querySelectorAll('.nav-menu a').forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('active');
        hamburger.classList.remove('active');
    });
});

// Smooth scroll for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href === '#') return; // skip empty anchors
        e.preventDefault();
        const target = document.querySelector(href);
        if (!target) return;
        const headerOffset = 80;
        const elementPosition = target.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
        window.scrollTo({
            top: offsetPosition,
            behavior: 'smooth'
        });
    });
});

// Article "Citește mai mult" toggle
document.querySelectorAll('.read-more').forEach(btn => {
    btn.addEventListener('click', function(e) {
        e.preventDefault();
        const card = this.closest('.news-card');
        const full = card.querySelector('.article-full');
        if (!full) return;

        if (full.classList.contains('open')) {
            full.classList.remove('open');
            this.textContent = 'Citește mai mult →';
        } else {
            // Close other open articles
            document.querySelectorAll('.article-full.open').forEach(open => {
                open.classList.remove('open');
                const otherBtn = open.closest('.news-card').querySelector('.read-more');
                if (otherBtn) otherBtn.textContent = 'Citește mai mult →';
            });
            full.classList.add('open');
            this.textContent = 'Închide ↑';
        }
    });
});

// Navbar background change on scroll
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.background = 'rgba(255,255,255,0.98)';
    } else {
        navbar.style.background = 'var(--white)';
    }
});

// Intersection Observer for animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe all cards and sections
document.querySelectorAll('.news-card, .training-card, .nutrition-card, .profile-card').forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
    observer.observe(card);
});

// Active navigation link highlighting
const sections = document.querySelectorAll('section[id]');
window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        if (pageYOffset >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });
    document.querySelectorAll('.nav-menu a').forEach(link => {
        link.style.color = '';
        if (link.getAttribute('href') === `#${current}`) {
            link.style.color = '#e63946';
        }
    });
});

// Performance: Lazy loading for images
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('img').forEach(img => {
        img.setAttribute('loading', 'lazy');
    });
});

// Console welcome
console.log('%c800m Athletics', 'color: #e63946; font-size: 24px; font-weight: bold;');
console.log('%cGhidul tău pentru proba de 800m — 800m.ro', 'color: #1d3557; font-size: 14px;');
