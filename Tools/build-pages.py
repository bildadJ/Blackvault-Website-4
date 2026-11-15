#!/usr/bin/env python3
"""Generates sector, intelligence and portal-gateway pages from one template. Run, then run build-nav.py."""
import os
from html import escape as e
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SVG='<svg viewBox="0 0 100 100"><g><g fill="none" stroke="#C2A878" stroke-width="1"><path d="M10 50L50 10L90 50L50 90Z"/><path d="M10 50H90M50 10V90M30 30L70 70M70 30L30 70"/></g><g fill="#C2A878"><circle cx="50" cy="10" r="3"/><circle cx="90" cy="50" r="3"/><circle cx="50" cy="90" r="3"/><circle cx="10" cy="50" r="3"/><circle cx="50" cy="50" r="4"/></g></g></svg>'
def page(fn,title,desc,theme,body,foot,noindex=False):
    rb='<meta name="robots" content="noindex, nofollow">\n' if noindex else ''
    h=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)} | Blackvault</title>
<meta name="description" content="{e(desc)}">
{rb}<meta name="theme-color" content="#141413">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="canonical" href="https://blackvault.co.ke/{fn}">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<meta property="og:title" content="{e(title)} | Blackvault">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
<meta property="og:image" content="https://blackvault.co.ke/assets/og-image.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Inter:wght@400;500;600&display=swap">
<link rel="stylesheet" href="assets/styles.css">
</head>
<body{' class="'+theme+'"' if theme else ''}>
<a class="sr" href="#main">Skip to content</a>
<header></header>
<main id="main">
{body}
</main>
<footer><img src="assets/logo-lockup.svg" alt="Blackvault" width="125" height="22"><p>&copy; <span class="y"></span> Blackvault. All rights reserved. {e(foot)}</p></footer>
<script src="assets/main.js"></script>
</body>
</html>
'''
    open(os.path.join(R,fn),"w",encoding="utf-8").write(h)
def rows(items): return "".join(f'<div class="row n rv"><span class="num">{i+1:02d}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i,(t,d) in enumerate(items))
def dl(items): return "<dl>"+"".join(f'<div class="rv"><dt>{e(t)}</dt><dd>{e(d)}</dd></div>' for t,d in items)+"</dl>"
def hero(p,label,h1,sub,b1,b2,strip):
    return f'<section class="dk hero sh u1" id="{p}-top"><div class="mk" aria-hidden="true">{SVG}</div><p class="lb">{label}</p><h1>{h1}</h1><p class="sub">{e(sub)}</p><div>{b1}{b2}</div><div class="strip">{strip}</div></section>'
def over(p,lead,para,status): return f'<section id="{p}-overview"><div class="two"><div class="rv"><p class="lb">Overview</p><h2>{status[0]}</h2></div><div class="rv"><p class="lead">{e(lead)}</p><p>{e(para)}</p><div class="box2"><strong>Status:</strong> {e(status[1])}</div></div></div></section>'
def contact(p,h,t,extra):
    return f'<section class="dk" id="{p}-contact"><div class="cg"><div><p class="lb">Stay in touch</p><h2 class="u4">{e(h)}</h2><p>{e(t)}</p></div><div class="ct"><a data-mail="partners" href="#"><small>Strategic partnerships</small><span></span></a><a data-mail="general" href="#"><small>General enquiries</small><span></span></a>{extra}</div></div></section>'
# ---------- sectors
SEC=[("finance-capital","fin","th-fin","Finance and Capital","Capital markets reward <i>patience</i> and punish haste.","A Blackvault venture area in development, built on research discipline and restraint in how capital is allocated.",
 "Finance and Capital is the area where Blackvault intends to develop its research and capital allocation capability.","It is being shaped around one idea: conviction should be earned through work. Research comes first, and capital follows only where judgement can be defended.","No financial products, funds or advisory services have been launched. This page describes intended direction only.",
 [("Research and market intelligence","Building the analytical discipline to understand markets, instruments and risk before committing capital."),("Capital allocation","A framework for weighing opportunities against each other, including the cost of not choosing them."),("Partnerships and structures","Relationships and structures suited to long-horizon investment.")],
 [("Research before capital","No position without a documented view of what must be true."),("Restraint","Declining is a valid decision when the evidence is uncertain."),("Governance first","Controls and accountability before scale.")]),
 ("energy-resources","en","th-en","Energy and Resources","Energy and resources underpin <i>every</i> other sector.","A Blackvault venture area in development, examining how to participate responsibly across cycles, regulation and transition.",
 "Energy and Resources is an area Blackvault is studying before any commitment.","Cycles, regulation and the energy transition shape this sector more than most. We intend to understand them thoroughly and enter only where we can add real judgement.","No energy or resource assets have been acquired and no projects launched. This page describes intended direction only.",
 [("Energy for operations","Practical, reliable energy supporting agriculture, storage and processing."),("Natural resources","Understanding resource value chains, licensing and regulatory exposure."),("Transition","How changing energy systems create and remove opportunity.")],
 [("Understand the cycle","Commodity and policy cycles are studied before capital is considered."),("Regulation as a variable","Licensing and compliance are treated as core risks."),("Responsible participation","Environmental and community impact are part of the assessment.")]),
 ("infrastructure-industrial","inf","th-inf","Infrastructure and Industrial Development","Roads, power, storage and production capacity <i>compound</i> for generations.","A Blackvault venture area in development, suited to long-horizon capital and patient execution.",
 "Infrastructure and Industrial Development is an area Blackvault intends to approach slowly and with partners.","Assets in this sector are long-lived, capital-intensive and closely tied to public policy. They reward careful structuring and punish optimism.","No infrastructure or industrial assets are held and no projects have been launched. This page describes intended direction only.",
 [("Storage and logistics","Capacity that reduces loss and improves market access for producers."),("Production capacity","Industrial facilities that add value close to source."),("Enabling infrastructure","Power, water and transport that unlock other ventures.")],
 [("Long horizons","Returns are assessed over decades, not quarters."),("Partner-led structures","Projects are structured with specialist partners and clear accountability."),("Downside first","We ask what could go wrong, and how badly, before anything else.")])]
for fn,p,th,name,h1,sub,lead,para,stat,foc,app in SEC:
    b=hero(p,'A Blackvault venture area &middot; <span class="dev">In development</span>',h1,sub,f'<a class="btn" href="#{p}-focus">What we are exploring</a>','<a class="btn q" href="index.html#ventures">All ventures &rarr;</a>',f'<span>{e(name)}</span><span>Coming soon</span>')
    b+=over(p,lead,para,("In development",stat))+f'<section class="u7" id="{p}-focus"><p class="lb">What we are exploring</p><h2 class="u3">Areas of focus</h2>{rows(foc)}</section>'
    b+=f'<section class="ch" id="{p}-approach"><p class="lb">Our approach</p><h2 class="u3">How we will build it</h2>{dl(app)}</section>'
    b+=contact(p,"Interested in this area?","If you share a long-term view of this sector, we would be glad to hear from you.",'<a href="agri-ventures.html"><small>Our first venture</small><span>Explore Blackvault Agri Ventures Ltd</span></a>')
    page(fn+".html",name,f"{name}: a Blackvault venture area in development.",th,b,f"{name} is an area in development and not an operating business.")
# ---------- intelligence
INT=[("financial-intelligence","fi","Financial Intelligence Centre","Financial intelligence for <i>disciplined</i> decisions.","Markets, instruments and capital structures, examined with primary evidence.",
 "The Financial Intelligence Centre is where Blackvault will publish its work on financial markets and institutions.","It will cover how capital is priced, structured and risked, with analysis meant to be checked, not merely read.",
 [("Equities and valuation","Company and market valuation, earnings analysis and screening methods."),("Fixed income and money markets","Government securities, yield curves, credit and liquidity."),("Currencies and commodities","Exchange rates, commodity cycles and external-sector linkages."),("Capital structures","Funding, leverage, private equity and portfolio construction.")]),
 ("economics-research","er","Economics Research Centre","Economics research grounded in <i>Kenya</i>, Africa and the world.","Macroeconomic analysis covering growth, inflation, policy, debt and trade.",
 "The Economics Research Centre will study the forces that shape the environment in which ventures operate.","Kenyan and African economics will be treated as primary subjects, set within global conditions.",
 [("Growth and inflation","Output, prices and the drivers behind them."),("Monetary and fiscal policy","Interest rates, budgets, taxation and their effects."),("Public debt and the external sector","Debt sustainability, balance of payments and exchange rates."),("Trade and regional integration","Regional markets, trade policy and supply chains.")]),
 ("sector-industry-intelligence","si","Sector and Industry Intelligence","Understand a sector <i>before</i> entering it.","Industry structure, economics and outlooks across the sectors that matter to the group.",
 "Sector and Industry Intelligence is the discipline behind Blackvault's decisions to enter, wait or decline.","Each sector will be examined for structure, economics, regulation and risk before it is considered for a venture.",
 [("Agriculture and agribusiness","Value chains, pricing, seasonality and market access."),("Energy, mining and resources","Cycles, licensing and transition."),("Financial services and technology","Market structure and business models."),("Manufacturing, real estate, infrastructure and logistics","Capacity, asset economics and enabling systems.")]),
 ("strategic-market-analysis","sm","Strategic Market Analysis","Positioning, competition and <i>market</i> structure.","How markets are organised, who holds advantage and where durable positions can be built.",
 "Strategic Market Analysis connects research to action by asking where Blackvault could hold a defensible position.","It will examine demand, competitive dynamics, barriers and partnerships in specific markets.",
 [("Demand and customers","Who buys, why, and how that is changing."),("Competitive dynamics","Incumbents, entrants and sources of advantage."),("Barriers and regulation","What protects or limits a position."),("Partnership routes","Where partners can strengthen a position.")]),
 ("investment-research","ir","Investment Research","Investment research that states what must be <i>true</i>.","Theses, assumptions and risks set out so that others can test them.",
 "Investment Research will present Blackvault's views in a form that can be examined and challenged.","Each piece will state its thesis, evidence, assumptions and what would change the view.",
 [("Thesis and evidence","A clear claim and the facts that support it."),("Valuation and returns","How value and expected return were assessed."),("Risks and downside","What could go wrong and how badly."),("Monitoring","What to watch and when to revisit.")]),
 ("emerging-opportunities","eo","Emerging Opportunities","Early signals worth <i>watching</i>.","A watch-list of developing industries, technologies and shifts, before they become obvious.",
 "Emerging Opportunities records early signals and the reasoning for taking them seriously or setting them aside.","Signals here are observations, not recommendations, and are tracked until the evidence supports a view.",
 [("Emerging industries","New sectors and business models taking shape."),("Technology shifts","Tools changing the economics of existing industries."),("Policy and demand changes","Developments that open or close opportunities."),("Signals under review","Ideas tracked but not yet supported by evidence.")])]
LINKS="".join(f'<li><a href="{f}.html">{e(n)}</a></li>' for f,_,n,*_ in INT)
for fn,p,name,h1,sub,lead,para,cov in INT:
    b=hero(p,'Research Centre &middot; <span class="dev">In preparation</span>',h1,sub,f'<a class="btn" href="#{p}-scope">Scope</a>','<a class="btn q" href="research.html#res-library">Research library &rarr;</a>',f'<span>{e(name)}</span><span>Blackvault Research</span>')
    b+=over(p,lead,para,("Scope and status","No publications have been issued under this centre yet. Nothing is shown here until real research is published."))
    b+=f'<section class="u7" id="{p}-scope"><p class="lb">Intended coverage</p><h2 class="u3">What we will cover</h2>{rows(cov)}</section>'
    b+=f'<section class="ch" id="{p}-standards"><p class="lb">Research standards</p><h2 class="u3">How it will be published</h2>'+dl([("Named and dated","Every publication carries an author or issuing department and a date."),("Sources shown","Data and sources are identified so claims can be checked."),("No placeholder research","We do not publish filler. The library stays empty until there is something real.")])+'</section>'
    b+=f'<section id="{p}-more"><p class="lb">Intelligence and Research Centre</p><h2 class="u2">Other research areas</h2><ul class="cats">{LINKS}<li><a href="research.html">Research centre overview</a></li></ul></section>'
    b+=contact(p,"Questions or collaboration","If you would like to contribute to or comment on this area of research, we would be glad to hear from you.",'<a href="research.html#res-briefing"><small>Blackvault Briefing</small><span>Register interest</span></a>')
    page(fn+".html",name,f"{name}: a research area of the Blackvault Intelligence and Research Centre.","th-fin",b,"This page describes intended practice and contains no performance data.")
# ---------- portals
def portal(fn,p,name,who,how,area):
    b=hero(p,f'Restricted access &middot; <span class="dev">By invitation</span>',f'{e(name)}',f'For {who}.',f'<a class="btn" href="#{p}-access">How access works</a>','<a class="btn q" href="index.html#contact">Request access &rarr;</a>','<span>Restricted</span><span>Authorised users only</span>')
    b+=f'<section id="{p}-access"><div class="two"><div class="rv"><p class="lb">Access</p><h2>Authenticated entry</h2></div><div class="rv"><p class="lead">{e(how)}</p><p>Access is granted by Blackvault to named individuals. There is no public registration, and no password is stored on this website.</p><p><a class="btn" href="{area}">Continue to the area</a></p><div class="box2"><strong>Status:</strong> The portal is being prepared. Until access control is activated on the server, the area above contains no information.</div></div></div></section>'
    page(fn,name,f"{name}: restricted access for authorised users.","",b,"Access is by invitation only.",noindex=True)
portal("partner-portal.html","pp","Private Partner Portal","authorised Blackvault partners","Signing in is handled by an identity service in front of the website, using a one-time code sent to an approved email address.","partner-area.html")
portal("officials-portal.html","op","Officials Portal","authorised Blackvault officials","Signing in is handled by an identity service in front of the website, with stricter rules than the partner area and a separate approved list.","officials-area.html")
for fn,name,p in [("partner-area.html","Partner Area","pa"),("officials-area.html","Officials Area","oa")]:
    b=hero(p,'Authenticated area',name,"You have reached a protected area.",'','','<span>Restricted</span>')+f'<section id="{p}-s"><p class="lb">Status</p><h2 class="u4">Being prepared</h2><p>No documents or data are available here yet. Content will be added only after access control is verified.</p></section>'
    page(fn,name,f"{name} of Blackvault.","",b,"Restricted area.",noindex=True)
# ---------- forms: proposals, briefing, verification
def field(l,n,t="text",req=True,ac=""): return f'<label>{e(l)}<input name="{n}" type="{t}"{" required" if req else ""}{" autocomplete=%s"%chr(34)+ac+chr(34) if ac else ""}></label>'
def form(id_,subj,to,fields,btn,note):
    return f'<form data-form="{id_}" data-subject="{e(subj)}" data-to="{to}">{fields}<button class="btn" type="submit">{e(btn)}</button><p class="note">{e(note)}</p></form>'
def formpage(fn,p,name,label,h1,sub,rowsdata,stdtitle,std,formtitle,formtext,frm,status,foot,desc):
    b=hero(p,label,h1,sub,f'<a class="btn" href="#{p}-form">{e(formtitle)}</a>','<a class="btn q" href="index.html#contact">General enquiries &rarr;</a>',f'<span>{e(name)}</span><span>Blackvault</span>')
    b+=f'<section class="u7" id="{p}-about"><p class="lb">{e(rowsdata[0])}</p><h2 class="u3">{e(rowsdata[1])}</h2>{rows(rowsdata[2])}</section>'
    b+=f'<section id="{p}-std"><div class="two"><div class="rv"><p class="lb">{e(stdtitle)}</p><h2>{e(std[0])}</h2></div><div class="rv"><p class="lead">{e(std[1])}</p><div class="box2"><strong>Status:</strong> {e(status)}</div></div></div></section>'
    b+=f'<section class="dk" id="{p}-form"><div class="cg"><div><p class="lb">{e(formtitle)}</p><h2 class="u4">{e(formtext[0])}</h2><p>{e(formtext[1])}</p></div>{frm}</div></section>'
    page(fn,name,desc,"",b,foot)
SEL='<label>Type<select name="t"><option value="partners">Partnership enquiry</option><option value="business">Investment proposal</option><option value="partners">Strategic collaboration</option></select></label>'
formpage("submit.html","sb","Submit a Proposal",'Partnerships and opportunities &middot; <span class="dev">Reviewed by Blackvault</span>',"Bring us a proposal worth <i>examining.</i>","Partnership enquiries, investment proposals and strategic collaborations are all considered, and each receives a considered reply.",
 ("What you can submit","Three kinds of submission",[("Partnership enquiries","Organisations that wish to work with Blackvault or its ventures."),("Investment proposals","Opportunities seeking capital, with the case for why they endure."),("Strategic collaborations","Joint work in research, sourcing, markets or technology.")]),
 "How we review",("Our approach to proposals","We start by asking what must be true for an opportunity to endure, and we are prepared to decline. A clear, honest summary helps most. Include the problem, the market, who is involved, what you are asking of us, and the main risks."),
 "Submit a proposal",("Tell us what you have in mind","Describe the proposal briefly. We will reply to arrange any further material."),
 form("proposal","Blackvault proposal submission","partners",field("Name","n","text",True,"name")+field("Organisation","o","text",False,"organization")+field("Your email","e","email",True,"email")+SEL+field("Sector or industry","s","text",False)+'<label>Summary of the proposal<textarea name="m" rows="6" required></textarea></label>',"Send proposal","Please do not send confidential documents yet. Secure file upload is not available on this website. Describe the proposal and we will arrange a secure method. Submissions are sent by email."),
 "Secure document upload requires server-side storage and has not been set up. This form sends text only.","Submissions are reviewed at Blackvault's discretion and do not create any obligation.","Submit a partnership enquiry, investment proposal or strategic collaboration to Blackvault.")
formpage("briefing.html","br","Blackvault Briefing",'Corporate intelligence &middot; <span class="dev">Not yet launched</span>',"The Blackvault <i>Briefing.</i>","A recurring intelligence briefing bringing selected research, economic developments and announcements to subscribers.",
 ("What it will contain","Planned contents",[("Selected research","Highlights from the Intelligence and Research Centre, once published."),("Economic developments","Short commentary on developments that matter to our sectors."),("Corporate announcements","Official news from Blackvault and its ventures.")]),
 "Registering interest",("Be told when it starts","The Briefing has not launched, and no issue has been sent. Registering interest tells us you want it. We will write to you once it begins. Frequency and format will be confirmed at launch."),
 "Register interest",("Register your interest","Leave your name and email. We use it only to contact you about the Briefing."),
 form("briefing","Blackvault Briefing interest","general",field("Name","n","text",True,"name")+field("Your email","e","email",True,"email")+'<label>Interests (optional)<input name="m" type="text"></label>',"Register interest","Your details are sent to us by email. A subscriber list with confirmation emails will be set up before launch."),
 "The newsletter platform and double opt-in subscription have not yet been configured.","The Briefing has not launched. This page contains no research or performance data.","Register interest in the Blackvault Briefing, a corporate intelligence newsletter.")
formpage("verify.html","vf","Document Verification",'Corporate publications &middot; <span class="dev">Manual verification</span>',"Confirm a document is <i>genuine.</i>","If you hold a document that claims to come from Blackvault, we can confirm whether it is authentic.",
 ("How it will work","Reference and confirmation",[("Reference number","Official publications will carry a unique reference and issue date."),("Check against the record","The reference is compared with Blackvault's record of issued documents."),("Confirmation","You are told whether the document and its details match.")]),
 "Current method",("Verification by request","No automated checker exists yet, and this page does not pretend to give results. Send us the reference or description of the document and we will confirm, in writing, whether Blackvault issued it. Never rely on a document that cannot be confirmed."),
 "Request verification",("Ask us to confirm a document","Provide any reference number and the document's title and date."),
 form("verify","Blackvault document verification request","corporate",field("Your name","n","text",True,"name")+field("Your email","e","email",True,"email")+field("Reference number (if any)","r","text",False)+'<label>Document title, date and where you received it<textarea name="m" rows="5" required></textarea></label>',"Request verification","Your request is sent to us by email and answered by a person."),
 "An automated verification service requires a database and has not been built. Requests are checked by hand.","Blackvault has not yet issued numbered official documents; this page describes the intended process.","Ask Blackvault to confirm whether a document is authentic.")
