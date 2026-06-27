const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('.nav-links');
const navAnchors = document.querySelectorAll('.nav-links a');

navToggle.addEventListener('click', () => {
    const isOpen = navLinks.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', String(isOpen));
});

navAnchors.forEach((anchor) => {
    anchor.addEventListener('click', () => {
        navLinks.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
    });
});

const segmentData = [
    {
        title: '0-200m: prinde pozitia',
        text: 'Accelereaza curat, intra in culoarul interior cand este permis si gaseste un loc in primele pozitii fara sprint inutil.'
    },
    {
        title: '200-400m: stabilizeaza ritmul',
        text: 'Respira controlat si evita schimbarile dese de viteza. Trecerea la 400m trebuie sa fie rapida, dar nu disperata.'
    },
    {
        title: '400-600m: rezista la presiune',
        text: 'Aici cursa devine grea. Mentine cadenta, stai relaxat in umeri si pregateste pozitia pentru atacul final.'
    },
    {
        title: '600-800m: decide si ataca',
        text: 'Alege momentul clar: iesire din curba sau ultimii 100m. Bratele active si privirea sus te ajuta sa pastrezi forma.'
    }
];

document.querySelectorAll('.segment').forEach((button) => {
    button.addEventListener('click', () => {
        document.querySelectorAll('.segment').forEach((item) => item.classList.remove('active'));
        button.classList.add('active');

        const selected = segmentData[Number(button.dataset.segment)];
        document.querySelector('#segment-title').textContent = selected.title;
        document.querySelector('#segment-text').textContent = selected.text;
    });
});

const trainingPlans = {
    viteza: {
        title: 'Viteza si tehnica',
        description: 'Sesiuni scurte, recuperare mare, accent pe postura, contact rapid cu pista si relaxare la viteza.',
        items: [
            '6 x 80m accelerari progresive',
            '4 x 150m rapid, recuperare completa',
            'Drills: skipping, pendulare, alergare cu genunchii sus'
        ]
    },
    specific: {
        title: 'Specific pentru 800m',
        description: 'Intervale care simuleaza intensitatea cursei si invata corpul sa sustina ritmul cand oboseala creste.',
        items: [
            '3 x 500m la ritm de cursa, pauza 6 minute',
            '2 x 600m controlat + 2 x 200m rapid',
            '5 x 300m peste ritmul de cursa, pauza 3 minute'
        ]
    },
    baza: {
        title: 'Baza aeroba',
        description: 'Alergari usoare si tempo pentru recuperare mai buna intre repetari si stabilitate pe al doilea tur.',
        items: [
            '35-50 minute alergare usoara',
            '18-22 minute tempo confortabil-greu',
            '8 x 100m lansate dupa alergare usoara'
        ]
    }
};

document.querySelectorAll('.tab').forEach((tab) => {
    tab.addEventListener('click', () => {
        document.querySelectorAll('.tab').forEach((item) => {
            item.classList.remove('active');
            item.setAttribute('aria-selected', 'false');
        });

        tab.classList.add('active');
        tab.setAttribute('aria-selected', 'true');

        const plan = trainingPlans[tab.dataset.plan];
        document.querySelector('#plan-title').textContent = plan.title;
        document.querySelector('#plan-description').textContent = plan.description;
        document.querySelector('#plan-list').innerHTML = plan.items.map((item) => `<li>${item}</li>`).join('');
    });
});

const formatTime = (totalSeconds) => {
    if (totalSeconds < 60) {
        return `${totalSeconds.toFixed(2)}s`;
    }

    const minutes = Math.floor(totalSeconds / 60);
    const seconds = totalSeconds - minutes * 60;
    return `${minutes}:${seconds.toFixed(2).padStart(5, '0')}`;
};

const updateSplits = () => {
    const minutes = Number(document.querySelector('#minutes').value || 0);
    const seconds = Number(document.querySelector('#seconds').value || 0);
    const total = minutes * 60 + seconds;

    if (total <= 0) {
        return;
    }

    document.querySelector('#split-200').textContent = formatTime(total / 4);
    document.querySelector('#split-400').textContent = formatTime(total / 2);
    document.querySelector('#split-600').textContent = formatTime(total * 0.75);
    document.querySelector('#split-800').textContent = formatTime(total);
};

document.querySelector('#pace-form').addEventListener('submit', (event) => {
    event.preventDefault();
    updateSplits();
});

document.querySelectorAll('#minutes, #seconds').forEach((input) => {
    input.addEventListener('input', updateSplits);
});

const sections = document.querySelectorAll('main section[id]');

const setActiveLink = () => {
    let currentId = 'acasa';

    sections.forEach((section) => {
        const top = section.getBoundingClientRect().top;
        if (top <= 120) {
            currentId = section.id;
        }
    });

    navAnchors.forEach((anchor) => {
        anchor.classList.toggle('active', anchor.getAttribute('href') === `#${currentId}`);
    });
};

document.addEventListener('scroll', setActiveLink, { passive: true });
setActiveLink();
updateSplits();
