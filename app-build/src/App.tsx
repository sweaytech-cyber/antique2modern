import { useEffect, useRef, useState } from 'react';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { 
  Menu, X, MapPin, Phone, Mail, Clock, 
  Star, Package, Camera, Truck
} from 'lucide-react';
import './App.css';

gsap.registerPlugin(ScrollTrigger);

function App() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const mainRef = useRef<HTMLDivElement>(null);
  const heroRef = useRef<HTMLDivElement>(null);
  const aboutRef = useRef<HTMLDivElement>(null);
  const galleryRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const ctx = gsap.context(() => {
      // Hero entrance animation
      const heroTl = gsap.timeline();
      heroTl.fromTo('.hero-eyebrow', 
        { opacity: 0, x: -40 }, 
        { opacity: 1, x: 0, duration: 0.8, ease: 'power3.out' }
      )
      .fromTo('.hero-headline', 
        { opacity: 0, y: 24 }, 
        { opacity: 1, y: 0, duration: 0.8, ease: 'power3.out' }, 
        '-=0.5'
      )
      .fromTo('.hero-subheadline', 
        { opacity: 0, y: 20 }, 
        { opacity: 1, y: 0, duration: 0.7, ease: 'power3.out' }, 
        '-=0.5'
      )
      .fromTo('.hero-cta', 
        { opacity: 0, y: 16 }, 
        { opacity: 1, y: 0, duration: 0.6, ease: 'power3.out' }, 
        '-=0.4'
      )
      .fromTo('.hero-image', 
        { opacity: 0, x: 80, scale: 0.98 }, 
        { opacity: 1, x: 0, scale: 1, duration: 1, ease: 'power3.out' }, 
        '-=0.8'
      )
      .fromTo('.hero-scroll', 
        { opacity: 0, y: 10 }, 
        { opacity: 1, y: 0, duration: 0.5, ease: 'power3.out' }, 
        '-=0.4'
      );

      // Hero scroll-driven exit animation
      ScrollTrigger.create({
        trigger: heroRef.current,
        start: 'top top',
        end: '+=130%',
        pin: true,
        scrub: 0.6,
        onUpdate: (self) => {
          const progress = self.progress;
          if (progress > 0.7) {
            const exitProgress = (progress - 0.7) / 0.3;
            gsap.set('.hero-text-block', { 
              x: -18 * exitProgress + 'vw', 
              opacity: 1 - exitProgress * 0.75 
            });
            gsap.set('.hero-image', { 
              x: 18 * exitProgress + 'vw', 
              scale: 1 + 0.03 * exitProgress,
              opacity: 1 - exitProgress * 0.65 
            });
            gsap.set('.hero-scroll', { opacity: 1 - exitProgress });
          }
        }
      });

      // About section animation
      ScrollTrigger.create({
        trigger: aboutRef.current,
        start: 'top top',
        end: '+=130%',
        pin: true,
        scrub: 0.6,
        onUpdate: (self) => {
          const progress = self.progress;
          if (progress <= 0.3) {
            const entranceProgress = progress / 0.3;
            gsap.set('.about-headline', { 
              y: -10 * (1 - entranceProgress) + 'vh', 
              opacity: entranceProgress 
            });
            gsap.set('.about-image', { 
              y: 55 * (1 - entranceProgress) + 'vh', 
              scale: 0.96 + 0.04 * entranceProgress,
              opacity: entranceProgress 
            });
            gsap.set('.about-body', { 
              x: -10 * (1 - entranceProgress) + 'vw', 
              opacity: entranceProgress 
            });
          } else if (progress > 0.7) {
            const exitProgress = (progress - 0.7) / 0.3;
            gsap.set('.about-headline', { 
              y: -8 * exitProgress + 'vh', 
              opacity: 1 - exitProgress * 0.75 
            });
            gsap.set('.about-image', { 
              y: 18 * exitProgress + 'vh', 
              scale: 1 + 0.02 * exitProgress,
              opacity: 1 - exitProgress * 0.65 
            });
            gsap.set('.about-body', { x: -6 * exitProgress + 'vw', opacity: 1 - exitProgress });
          }
        }
      });

      // Gallery section animation
      ScrollTrigger.create({
        trigger: galleryRef.current,
        start: 'top top',
        end: '+=130%',
        pin: true,
        scrub: 0.6,
        onUpdate: (self) => {
          const progress = self.progress;
          if (progress <= 0.3) {
            const entranceProgress = progress / 0.3;
            gsap.set('.gallery-card-1', { 
              x: -60 * (1 - entranceProgress) + 'vw', 
              opacity: entranceProgress 
            });
            gsap.set('.gallery-card-2', { 
              y: 60 * (1 - entranceProgress) + 'vh', 
              opacity: entranceProgress 
            });
            gsap.set('.gallery-card-3', { 
              x: 60 * (1 - entranceProgress) + 'vw', 
              opacity: entranceProgress 
            });
          } else if (progress > 0.7) {
            const exitProgress = (progress - 0.7) / 0.3;
            gsap.set('.gallery-card-1', { 
              x: 18 * exitProgress + 'vw', 
              opacity: 1 - exitProgress * 0.75 
            });
            gsap.set('.gallery-card-2', { 
              scale: 1 - 0.08 * exitProgress, 
              opacity: 1 - exitProgress * 0.75 
            });
            gsap.set('.gallery-card-3', { 
              x: -18 * exitProgress + 'vw', 
              opacity: 1 - exitProgress * 0.75 
            });
          }
        }
      });

      // Flowing sections reveal
      gsap.utils.toArray<HTMLElement>('.reveal-section').forEach((section) => {
        gsap.fromTo(section, 
          { y: 30, opacity: 0 },
          {
            y: 0,
            opacity: 1,
            duration: 0.8,
            ease: 'power3.out',
            scrollTrigger: {
              trigger: section,
              start: 'top 80%',
              toggleActions: 'play none none reverse'
            }
          }
        );
      });

    }, mainRef);

    return () => ctx.revert();
  }, []);

  const scrollToSection = (sectionId: string) => {
    setMobileMenuOpen(false);
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  const testimonials = [
    { id: 1, quote: 'Eric and his team treated my mother\'s home with respect—and sold nearly everything in three days. Highly recommend for anyone in the Milwaukee area.', author: 'Rachel M.', role: 'Seller from Waukesha' },
    { id: 2, quote: 'Found a beautiful antique dresser at Antique 2 Modern. The piece was exactly as described and fairly priced. Worth the drive from Madison!', author: 'David L.', role: 'Buyer' },
    { id: 3, quote: 'Best estate sale company in Wisconsin. They handled my aunt\'s entire estate professionally and got us great prices.', author: 'Susan K.', role: 'Seller from Brookfield' },
  ];

  const faqs = [
    { q: 'How often does your inventory change?', a: 'Our inventory changes weekly as we process new estate acquisitions throughout southeastern Wisconsin. We recommend visiting often as our best pieces sell quickly!' },
    { q: 'Do you purchase individual items?', a: 'Yes! While most of our inventory comes from complete estate liquidations, we do consider individual pieces. Contact us for a free estimate.' },
    { q: 'What areas do you serve for estate sales?', a: 'We serve the greater Milwaukee area including New Berlin, Waukesha, Brookfield, and surrounding communities.' },
    { q: 'What types of items do you sell?', a: 'We carry everything from 1700s-era antiques to contemporary furniture, including art, home décor, lamps, collectibles, and more.' },
  ];

  return (
    <div ref={mainRef} className="relative">
      {/* Grain Overlay */}
      <div className="grain-overlay" />
      
      {/* Navigation */}
      <nav className="fixed top-0 left-0 right-0 z-50 bg-[#F4F1EA]/90 backdrop-blur-sm border-b border-[#1B1D21]/10">
        <div className="w-full px-6 lg:px-12 py-4 flex items-center justify-between">
          <button 
            onClick={() => scrollToSection('home')}
            className="font-display text-xl lg:text-2xl font-semibold text-[#1B1D21] tracking-tight"
          >
            Antique 2 Modern
          </button>
          
          {/* Desktop Nav */}
          <div className="hidden lg:flex items-center gap-8">
            <button onClick={() => scrollToSection('about')} className="font-ui text-sm text-[#1B1D21] hover:text-[#C69B3C] transition-colors">About</button>
            <button onClick={() => scrollToSection('services')} className="font-ui text-sm text-[#1B1D21] hover:text-[#C69B3C] transition-colors">Estate Sales</button>
            <button onClick={() => scrollToSection('sell')} className="font-ui text-sm text-[#1B1D21] hover:text-[#C69B3C] transition-colors">Sell to Us</button>
            <button onClick={() => scrollToSection('contact')} className="font-ui text-sm text-[#1B1D21] hover:text-[#C69B3C] transition-colors">Contact</button>
          </div>
          
          {/* Mobile Menu Button */}
          <button 
            className="lg:hidden p-2"
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
          >
            {mobileMenuOpen ? <X size={24} /> : <Menu size={24} />}
          </button>
        </div>
        
        {/* Mobile Menu */}
        {mobileMenuOpen && (
          <div className="lg:hidden bg-[#F4F1EA] border-t border-[#1B1D21]/10 px-6 py-6 flex flex-col gap-4">
            <button onClick={() => scrollToSection('about')} className="font-ui text-sm text-[#1B1D21] py-2 text-left">About</button>
            <button onClick={() => scrollToSection('services')} className="font-ui text-sm text-[#1B1D21] py-2 text-left">Estate Sales</button>
            <button onClick={() => scrollToSection('sell')} className="font-ui text-sm text-[#1B1D21] py-2 text-left">Sell to Us</button>
            <button onClick={() => scrollToSection('contact')} className="font-ui text-sm text-[#1B1D21] py-2 text-left">Contact</button>
          </div>
        )}
      </nav>

      {/* Section 1: Hero */}
      <section id="home" ref={heroRef} className="section-pinned bg-[#F4F1EA] z-10">
        <div className="absolute inset-0 flex items-center">
          {/* Text Block */}
          <div className="hero-text-block absolute left-[7vw] top-[18vh] w-[38vw] z-10">
            <p className="hero-eyebrow text-eyebrow text-[#6E7279] mb-6">
              Estate Sales & Curated Furniture
            </p>
            <h1 className="hero-headline font-display text-[clamp(44px,5.2vw,84px)] text-[#1B1D21] mb-6 leading-[0.92]">
              Find the piece with a past.
            </h1>
            <p className="hero-subheadline font-body text-[clamp(15px,1.15vw,18px)] text-[#6E7279] leading-relaxed max-w-md mb-8">
              A local estate sale company in New Berlin, WI helping families downsize and liquidate estates. 
              Shop our ever-changing inventory of 1700s-era antiques to contemporary furniture.
            </p>
            <div className="hero-cta flex flex-col sm:flex-row gap-4 items-start">
              <button 
                onClick={() => scrollToSection('contact')}
                className="btn-primary"
              >
                Request an Estate Consultation
              </button>
            </div>
          </div>
          
          {/* Hero Image - Real Store Photo */}
          <div className="hero-image absolute left-[52vw] top-[14vh] w-[41vw] h-[72vh] image-card card-shadow">
            <img 
              src="/images/a2m_store_1.jpg" 
              alt="Antique 2 Modern store interior" 
              className="w-full h-full object-cover"
            />
          </div>
          
          {/* Scroll Hint */}
          <div className="hero-scroll absolute left-[7vw] bottom-[8vh] flex flex-col items-start gap-2">
            <span className="font-ui text-xs text-[#6E7279] tracking-widest uppercase">Scroll</span>
            <div className="w-[60px] h-[2px] bg-[#C69B3C]" />
          </div>
        </div>
      </section>

      {/* Section 2: About Us */}
      <section id="about" ref={aboutRef} className="section-pinned bg-[#F4F1EA] z-20">
        <div className="absolute inset-0 flex flex-col items-center justify-center lg:justify-start">
          <h2 className="about-headline absolute top-[14vh] left-1/2 -translate-x-1/2 lg:absolute lg:left-1/2 lg:top-[14vh] font-display text-[clamp(34px,3.6vw,56px)] text-[#1B1D21] text-center w-[72vw] lg:w-[72vw]">
            Who We Are
          </h2>
          
          <div className="about-image absolute top-[34vh] left-1/2 -translate-x-1/2 lg:absolute lg:left-1/2 lg:top-[34vh] w-[72vw] lg:w-[72vw] h-[44vh] lg:h-[44vh] image-card card-shadow">
            <img 
              src="/images/a2m_store_2.jpg" 
              alt="Antique 2 Modern showroom" 
              className="w-full h-full object-cover"
            />
          </div>
          
          <p className="about-body absolute left-[7vw] bottom-[10vh] lg:absolute lg:left-[7vw] lg:bottom-[10vh] w-[40vw] lg:w-[40vw] font-body text-[clamp(15px,1.15vw,18px)] text-[#6E7279] leading-relaxed">
            Antique 2 Modern is a local estate sale company that helps families and individuals downsize and liquidate their estates. 
            Our store offers gently used furniture and furnishings collected from these estates. 
            Our inventory changes weekly, so customers are encouraged to visit often.
          </p>
          
          <div className="absolute right-[7vw] bottom-[10vh] lg:absolute lg:right-[7vw] lg:bottom-[10vh] w-[34vw] lg:w-[34vw] font-body text-[clamp(15px,1.15vw,18px)] text-[#6E7279] leading-relaxed hidden lg:block">
            <p className="mb-4">
              <strong className="text-[#1B1D21]">What We Sell:</strong>
            </p>
            <ul className="space-y-2">
              <li>• 1700s-era antiques</li>
              <li>• Vintage furniture</li>
              <li>• Modern and contemporary furniture</li>
              <li>• Artwork and home décor</li>
              <li>• Lamps and unique collectibles</li>
            </ul>
          </div>
        </div>
      </section>

      {/* Section 3: Gallery */}
      <section id="services" ref={galleryRef} className="section-pinned bg-[#F4F1EA] z-30">
        <div className="absolute inset-0 flex flex-col items-center pt-[10vh] lg:pt-[10vh] @md:pt-[5vh] @sm:pt-[2rem] px-4 lg:px-0">
          <h2 className="font-display text-[clamp(34px,3.6vw,56px)] text-[#1B1D21] mb-8">Our Store</h2>
          
          <div className="flex flex-col lg:flex-row items-center justify-center gap-[4vw] lg:gap-[4vw] px-[7vw] lg:px-[7vw] w-full">
            {/* Store Photo 1 */}
            <div className="gallery-card-1 w-full lg:w-[26vw] h-[300px] lg:h-[60vh] image-card card-shadow relative group">
              <img 
                src="/images/a2m_store_3.jpg" 
                alt="Antique 2 Modern store" 
                className="w-full h-full object-cover"
              />
            </div>
            
            {/* Store Photo 2 */}
            <div className="gallery-card-2 w-full lg:w-[26vw] h-[300px] lg:h-[60vh] image-card card-shadow relative group">
              <img 
                src="/images/a2m_store_4.jpg" 
                alt="Antique 2 Modern furniture" 
                className="w-full h-full object-cover"
              />
            </div>
            
            {/* Store Photo 3 */}
            <div className="gallery-card-3 w-full lg:w-[26vw] h-[300px] lg:h-[60vh] image-card card-shadow relative group">
              <img 
                src="/images/a2m_store_1.jpg" 
                alt="Antique 2 Modern interior" 
                className="w-full h-full object-cover"
              />
            </div>
          </div>
        </div>
      </section>

      {/* Section 4: Testimonials (Flowing) */}
      <section className="reveal-section bg-[#F4F1EA] py-20 lg:py-32 z-40 relative">
        <div className="w-full px-6 lg:px-[7vw]">
          <h2 className="font-display text-[clamp(34px,3.6vw,56px)] text-[#1B1D21] mb-12 text-center">
            What sellers & buyers say
          </h2>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {testimonials.map((t) => (
              <div key={t.id} className="bg-white rounded-[10px] p-8 card-shadow">
                <div className="flex gap-1 mb-4">
                  {[...Array(5)].map((_, i) => (
                    <Star key={i} size={16} className="fill-[#C69B3C] text-[#C69B3C]" />
                  ))}
                </div>
                <p className="font-body text-[#1B1D21] mb-6 leading-relaxed">"{t.quote}"</p>
                <div>
                  <p className="font-ui text-sm font-medium text-[#1B1D21]">{t.author}</p>
                  <p className="font-ui text-xs text-[#6E7279]">{t.role}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Section 5: Sell to Us (Flowing) */}
      <section id="sell" className="reveal-section bg-[#F4F1EA] py-20 lg:py-32 z-50 relative border-t border-[#1B1D21]/10">
        <div className="w-full px-6 lg:px-[7vw]">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-20">
            <div>
              <h2 className="font-display text-[clamp(34px,3.6vw,56px)] text-[#1B1D21] mb-4">
                Sell to Us
              </h2>
              <p className="font-body text-[clamp(15px,1.15vw,18px)] text-[#6E7279] leading-relaxed mb-8">
                Have antiques or vintage furniture to sell? We purchase individual pieces and complete estates. 
                Get a free, no-obligation estimate.
              </p>
              
              <div className="space-y-6">
                <div className="flex items-start gap-4">
                  <div className="w-10 h-10 rounded-full bg-[#C69B3C]/10 flex items-center justify-center flex-shrink-0">
                    <Camera size={20} className="text-[#C69B3C]" />
                  </div>
                  <div>
                    <h4 className="font-display text-lg text-[#1B1D21] mb-1">Send Photos</h4>
                    <p className="font-body text-sm text-[#6E7279]">Take clear photos and email them to us</p>
                  </div>
                </div>
                
                <div className="flex items-start gap-4">
                  <div className="w-10 h-10 rounded-full bg-[#C69B3C]/10 flex items-center justify-center flex-shrink-0">
                    <Package size={20} className="text-[#C69B3C]" />
                  </div>
                  <div>
                    <h4 className="font-display text-lg text-[#1B1D21] mb-1">Get an Estimate</h4>
                    <p className="font-body text-sm text-[#6E7279]">We'll assess and provide a fair offer within 48 hours</p>
                  </div>
                </div>
                
                <div className="flex items-start gap-4">
                  <div className="w-10 h-10 rounded-full bg-[#C69B3C]/10 flex items-center justify-center flex-shrink-0">
                    <Truck size={20} className="text-[#C69B3C]" />
                  </div>
                  <div>
                    <h4 className="font-display text-lg text-[#1B1D21] mb-1">We Pick Up</h4>
                    <p className="font-body text-sm text-[#6E7279]">We handle pickup and payment—quick and easy</p>
                  </div>
                </div>
              </div>
            </div>
            
            <div className="bg-white rounded-[10px] p-8 card-shadow">
              <h3 className="font-display text-2xl text-[#1B1D21] mb-6">Request a Free Estimate</h3>
              <form className="space-y-4">
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <input 
                    type="text" 
                    placeholder="First Name" 
                    className="w-full px-4 py-3 rounded-lg border border-[#1B1D21]/10 font-body text-sm focus:outline-none focus:border-[#C69B3C]"
                  />
                  <input 
                    type="text" 
                    placeholder="Last Name" 
                    className="w-full px-4 py-3 rounded-lg border border-[#1B1D21]/10 font-body text-sm focus:outline-none focus:border-[#C69B3C]"
                  />
                </div>
                <input 
                  type="email" 
                  placeholder="Email Address" 
                  className="w-full px-4 py-3 rounded-lg border border-[#1B1D21]/10 font-body text-sm focus:outline-none focus:border-[#C69B3C]"
                />
                <input 
                  type="tel" 
                  placeholder="Phone Number" 
                  className="w-full px-4 py-3 rounded-lg border border-[#1B1D21]/10 font-body text-sm focus:outline-none focus:border-[#C69B3C]"
                />
                <textarea 
                  placeholder="Tell us about your items..." 
                  rows={4}
                  className="w-full px-4 py-3 rounded-lg border border-[#1B1D21]/10 font-body text-sm focus:outline-none focus:border-[#C69B3C] resize-none"
                />
                <button type="button" className="btn-gold w-full">
                  Submit Request
                </button>
              </form>
            </div>
          </div>
        </div>
      </section>

      {/* Section 6: FAQ (Flowing) */}
      <section className="reveal-section bg-[#F4F1EA] py-20 lg:py-32 z-[60] relative border-t border-[#1B1D21]/10">
        <div className="w-full px-6 lg:px-[7vw]">
          <div className="max-w-3xl mx-auto">
            <h2 className="font-display text-[clamp(34px,3.6vw,56px)] text-[#1B1D21] mb-4 text-center">
              Customer Care
            </h2>
            <p className="font-body text-[clamp(15px,1.15vw,18px)] text-[#6E7279] text-center mb-12">
              Frequently asked questions about our services
            </p>
            
            <div className="space-y-4">
              {faqs.map((faq, i) => (
                <div key={i} className="bg-white rounded-[10px] p-6 card-shadow">
                  <h4 className="font-display text-lg text-[#1B1D21] mb-2">{faq.q}</h4>
                  <p className="font-body text-sm text-[#6E7279] leading-relaxed">{faq.a}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* Section 7: Contact & Footer */}
      <section id="contact" className="reveal-section bg-[#0E0F12] py-20 lg:py-24 z-[70] relative">
        <div className="w-full px-6 lg:px-[7vw]">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-20 mb-16">
            <div>
              <h2 className="font-display text-[clamp(34px,3.6vw,56px)] text-white mb-4">
                Visit Us Today
              </h2>
              <p className="font-body text-[clamp(15px,1.15vw,18px)] text-white/70 leading-relaxed mb-8">
                Stop by our showroom in New Berlin, Wisconsin. Our inventory changes weekly!
              </p>
              <div className="flex flex-col sm:flex-row gap-4">
                <button className="btn-gold">
                  Book a consultation
                </button>
                <button className="font-ui text-sm text-white hover:text-[#C69B3C] transition-colors flex items-center gap-2">
                  <Mail size={18} /> Send an email
                </button>
              </div>
            </div>
            
            <div className="space-y-6">
              <div className="flex items-start gap-4">
                <MapPin size={20} className="text-[#C69B3C] mt-1 flex-shrink-0" />
                <div>
                  <p className="font-ui text-sm text-white/50 mb-1">Address</p>
                  <p className="font-body text-white">13819 W National Ave, New Berlin, WI 53151</p>
                </div>
              </div>
              
              <div className="flex items-start gap-4">
                <Clock size={20} className="text-[#C69B3C] mt-1 flex-shrink-0" />
                <div>
                  <p className="font-ui text-sm text-white/50 mb-1">Hours</p>
                  <p className="font-body text-white">Tue–Sat, 10am–5pm</p>
                </div>
              </div>
              
              <div className="flex items-start gap-4">
                <Phone size={20} className="text-[#C69B3C] mt-1 flex-shrink-0" />
                <div>
                  <p className="font-ui text-sm text-white/50 mb-1">Phone</p>
                  <p className="font-body text-white">(262) 439-8085</p>
                </div>
              </div>
            </div>
          </div>
          
          {/* Footer */}
          <div className="pt-8 border-t border-white/10 flex flex-col lg:flex-row items-center justify-between gap-6">
            <p className="font-ui text-sm text-white/50">
              © Antique 2 Modern. All rights reserved.
            </p>
            
            <div className="flex items-center gap-6">
              <button className="font-ui text-sm text-white/50 hover:text-white transition-colors">Privacy</button>
              <button className="font-ui text-sm text-white/50 hover:text-white transition-colors">Terms</button>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}

export default App;
