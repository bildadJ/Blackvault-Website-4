/* CONFIGURE: replace these with your real addresses before launch */
var CONFIG={general:"enquiries@blackvault.co.ke",business:"enquiries@blackvault.co.ke",partners:"enquiries@blackvault.co.ke",corporate:"enquiries@blackvault.co.ke",agri:"agri@blackvault.co.ke"};
/* OPTIONAL: paste a Formspree URL (https://formspree.io/f/xxxx) to send the form directly instead of opening the visitor's email app */
var FORM_ENDPOINT="https://formspree.io/f/xyewejnj";
var $=function(s){return Array.prototype.slice.call(document.querySelectorAll(s))};
$(".y").forEach(function(e){e.textContent=new Date().getFullYear()});
$("[data-mail]").forEach(function(a){var m=CONFIG[a.dataset.mail];a.href="mailto:"+m;var s=a.querySelector("span");if(s)s.textContent=m});
var hs=$("header");function sc(){hs.forEach(function(h){h.classList.toggle("s",scrollY>40)})}sc();addEventListener("scroll",sc,{passive:true});
hs.forEach(function(h){var b=h.querySelector(".mb"),n=h.querySelector("nav");
function set(o){n.classList.toggle("o",o);b.setAttribute("aria-expanded",o);b.textContent=o?"CLOSE":"MENU";document.body.style.overflow=o?"hidden":"";if(o)h.classList.add("s")}
b.onclick=function(){set(!n.classList.contains("o"))};
n.querySelectorAll("a").forEach(function(a){a.addEventListener("click",function(){set(false)})});
addEventListener("keydown",function(e){if(e.key==="Escape"&&n.classList.contains("o")){set(false);b.focus()}});
addEventListener("resize",function(){if(innerWidth>900&&n.classList.contains("o"))set(false)})});
if("IntersectionObserver" in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add("on");io.unobserve(e.target)}})},{threshold:.12});$(".rv").forEach(function(e){io.observe(e)})}else{$(".rv").forEach(function(e){e.classList.add("on")})}
var f=document.getElementById("f");if(f)f.onsubmit=function(ev){ev.preventDefault();var d=new FormData(ev.target),to=CONFIG[d.get("t")],st=f.querySelector(".note");
if(FORM_ENDPOINT){d.append("_to",to);fetch(FORM_ENDPOINT,{method:"POST",body:d,headers:{Accept:"application/json"}}).then(function(r){if(!r.ok)throw 0;f.reset();st.textContent="Thank you. Your message has been sent."}).catch(function(){st.textContent="Sorry, that did not send. Please email us directly."});return}
location.href="mailto:"+to+"?subject="+encodeURIComponent("Website enquiry from "+d.get("n"))+"&body="+encodeURIComponent(d.get("m")+"\n\nReply to: "+d.get("e"))};
/* highlight current section in nav */
if("IntersectionObserver" in window){var ls=$("header nav a[href^='#']"),so=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){ls.forEach(function(a){a.style.color=a.getAttribute("href")==="#"+e.target.id?"var(--g)":""})}})},{rootMargin:"-45% 0px -50% 0px"});ls.forEach(function(a){var t=document.querySelector(a.getAttribute("href"));if(t)so.observe(t)})}

/* rail progress */
function pg(){var d=document.documentElement,m=d.scrollHeight-innerHeight;hs.forEach(function(h){h.style.setProperty("--p",m>0?(scrollY/m).toFixed(3):0)})}pg();addEventListener("scroll",pg,{passive:true});
/* ventures: master-detail on desktop */
if(document.getElementById("ventures")&&matchMedia("(min-width:901px)").matches){
var rows=$("#ventures .row"),w=document.createElement("div"),l=document.createElement("div"),p=document.createElement("aside");
w.className="vwrap";l.className="vlist";p.className="vp";p.setAttribute("aria-hidden","true");
rows[0].parentNode.insertBefore(w,rows[0]);w.appendChild(l);w.appendChild(p);rows.forEach(function(r){l.appendChild(r)});
function show(r){rows.forEach(function(x){x.classList.toggle("act",x===r)});p.innerHTML="";p.appendChild(r.querySelector("svg").cloneNode(true));var h=document.createElement("div");h.className="vt";h.textContent=r.querySelector("h3").textContent;p.appendChild(h);var g=r.querySelector(".tag");if(g){var t=document.createElement("span");t.className="tag";t.textContent=g.textContent;p.appendChild(t)}}
rows.forEach(function(r){r.addEventListener("mouseenter",function(){show(r)});r.addEventListener("focusin",function(){show(r)})});show(rows[0])}
/* mission: words light up as you scroll */
if(!matchMedia("(prefers-reduced-motion:reduce)").matches){$(".mis").forEach(function(m){
function wrap(n){Array.prototype.slice.call(n.childNodes).forEach(function(c){if(c.nodeType===3){var f=document.createDocumentFragment();c.textContent.split(/(\s+)/).forEach(function(t){if(!t)return;if(/^\s+$/.test(t))f.appendChild(document.createTextNode(t));else{var s=document.createElement("span");s.className="w";s.textContent=t;f.appendChild(s)}});n.replaceChild(f,c)}else wrap(c)})}
wrap(m);m.classList.add("sw");var ws=m.querySelectorAll(".w");
function up(){var r=m.getBoundingClientRect(),q=Math.min(1,Math.max(0,(innerHeight*.85-r.top)/(r.height+innerHeight*.25))),k=Math.round(q*ws.length);for(var i=0;i<ws.length;i++)ws[i].classList.toggle("l",i<k)}
up();addEventListener("scroll",up,{passive:true})})}
/* tabs (pipeline) */
$("[data-tabs]").forEach(function(w){var bs=w.querySelectorAll(".tb"),ps=w.querySelectorAll(".tp");function go(i){bs.forEach(function(b,k){b.classList.toggle("act",k===i);b.setAttribute("aria-selected",k===i)});ps.forEach(function(p,k){p.hidden=k!==i})}bs.forEach(function(b,i){b.onclick=function(){go(i)};b.addEventListener("focus",function(){go(i)})});go(0)});

/* layered navigation: hover/click on desktop, accordion on mobile */
hs.forEach(function(h){var gs=h.querySelectorAll("nav li.g"),wide=function(){return matchMedia("(min-width:901px)").matches};
function set(g,o){gs.forEach(function(x){if(x!==g||!o){x.classList.remove("open");x.querySelector(".gb").setAttribute("aria-expanded","false")}});if(g&&o){g.classList.add("open");g.querySelector(".gb").setAttribute("aria-expanded","true")}}
gs.forEach(function(g){g.querySelector(".gb").addEventListener("click",function(){set(g,wide()?true:!g.classList.contains("open"))});g.addEventListener("mouseenter",function(){if(wide())set(g,true)})});
h.addEventListener("mouseleave",function(){if(wide())set(null,false)});
addEventListener("keydown",function(e){if(e.key==="Escape")set(null,false)});
document.addEventListener("click",function(e){if(wide()&&!h.contains(e.target))set(null,false)})});

/* generic forms (proposal, briefing, verification): Formspree if configured, otherwise opens the visitor's email app */
$("form[data-form]").forEach(function(fm){fm.onsubmit=function(ev){ev.preventDefault();var d=new FormData(fm),to=CONFIG[d.get("t")||fm.dataset.to]||CONFIG.general,st=fm.querySelector(".note"),sub=fm.dataset.subject+" - "+(d.get("n")||""),body=[];
fm.querySelectorAll("label").forEach(function(l){var i=l.querySelector("input,select,textarea");if(i&&i.name&&i.value)body.push(l.firstChild.textContent.trim()+": "+i.value)});
if(FORM_ENDPOINT){d.append("_to",to);d.append("_subject",sub);fetch(FORM_ENDPOINT,{method:"POST",body:d,headers:{Accept:"application/json"}}).then(function(r){if(!r.ok)throw 0;fm.reset();st.textContent="Thank you. Your message has been sent."}).catch(function(){st.textContent="Sorry, that did not send. Please email us directly."});return}
location.href="mailto:"+to+"?subject="+encodeURIComponent(sub)+"&body="+encodeURIComponent(body.join("\n\n"))}});
