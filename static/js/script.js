   document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });

        // Scroll animations
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

        document.querySelectorAll('.fade-in').forEach(el => {
            observer.observe(el);
        });

        // Header scroll effect
        // Ambil section home dan join
        const homeSection = document.querySelector('#home');
        const joinSection = document.querySelector('#join');

        window.addEventListener('scroll', () => {
            const header = document.querySelector('header');
            const logo = document.querySelector('.logo');
            const navLinks = document.querySelectorAll('.nav-links a');
            const scrollPos = window.scrollY + window.innerHeight / 2;
            const inHome = scrollPos >= homeSection.offsetTop && scrollPos < homeSection.offsetTop + homeSection.offsetHeight;
            const inJoin = scrollPos >= joinSection.offsetTop && scrollPos < joinSection.offsetTop + joinSection.offsetHeight;
            if (inHome || inJoin) {
                header.classList.remove('scrolled');
                logo.style.color = '#EDE8DC';
                navLinks.forEach(link => link.style.color = '#EDE8DC');
            } else {
                header.classList.add('scrolled');
                logo.style.color = '#ffffffff';
                navLinks.forEach(link => link.style.color = '#ffffffff');
            }
        });



        // Typing effect for hero text
        const heroTitle = document.querySelector('.hero-content h3');
        const originalText = heroTitle.textContent;
        heroTitle.textContent = '';
        
        setTimeout(() => {
            let i = 0;
            const typeWriter = () => {
                if (i < originalText.length) {
                    heroTitle.textContent += originalText.charAt(i);
                    i++;
                    setTimeout(typeWriter, 100);
                }
            };
            typeWriter();
        }, 1000);