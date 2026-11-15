#!/usr/bin/env python3
"""Single source of truth for the site navigation.
Edit MENU, run `python3 tools/build-nav.py`, and every page's <header> is regenerated.
A link is live only if its target file exists in the project root; otherwise it is
shown as 'In preparation' (never a dead link). Add the page, re-run, and it goes live."""
import os, re, glob
from html import escape as e
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MENU = [
 ("about","About","Identity and governance","Who we are, how we decide and how we allocate capital.",[
  ("About Blackvault","Why the group exists","index.html#about"),
  ("Mission and vision","What we are building toward","index.html#mission"),
  ("Corporate philosophy","How we think about capital","index.html#philosophy"),
  ("Governance framework","How decisions are made","governance.html"),
  ("Capital allocation","How we deploy capital","capital-allocation.html")]),
 ("ventures","Ventures","Ventures and opportunities","The enterprises we are building and the sectors we are studying.",[
  ("Blackvault Agri Ventures","Our first venture","agri-ventures.html"),
  ("Technology and innovation","Theme in development","technology-innovation.html"),
  ("Finance and capital","Theme in development","finance-capital.html"),
  ("Energy and resources","Theme in development","energy-resources.html"),
  ("Infrastructure and industrial","Theme in development","infrastructure-industrial.html"),
  ("Opportunities pipeline","How opportunities are assessed",None)]),
 ("intelligence","Intelligence","Intelligence and Research Centre","Independent research on markets, economies and industries.",[
  ("Research centre","Overview and approach","research.html"),
  ("Financial Intelligence Centre","Markets, instruments, capital structures","financial-intelligence.html"),
  ("Economics Research Centre","Kenya, Africa and global macro","economics-research.html"),
  ("Sector and industry intelligence","Industry structure and outlooks","sector-industry-intelligence.html"),
  ("Strategic market analysis","Positioning and competitive dynamics","strategic-market-analysis.html"),
  ("Investment research","Valuation and portfolio thinking","investment-research.html"),
  ("Emerging opportunities","Early signals worth watching","emerging-opportunities.html"),
  ("Research library","Publications as they are issued","research.html#res-library")]),
 ("publications","Publications","Publications and Briefing","Official documents, research papers and the Blackvault Briefing.",[
  ("Publications centre","Reports, papers, announcements","publications.html"),
  ("Blackvault Briefing","Corporate intelligence newsletter","briefing.html"),
  ("Document verification","Confirm an official document","verify.html")]),
 ("partners","Partners","Partnerships and access","Start a conversation, or sign in if you are an authorised partner or official.",[
  ("Start a conversation","Enquiries and opportunities","index.html#contact"),
  ("Submit a proposal","Investment and partnership proposals","submit.html"),
  ("Partner portal","Authorised partners only","partner-portal.html"),
  ("Officials portal","Authorised officials only","officials-portal.html")])]
def live(h): return bool(h) and os.path.exists(os.path.join(ROOT, h.split("#")[0]))
def header(page):
    out=[]
    for k,name,lab,desc,items in MENU:
        li=[]; cur=False
        for t,d,h in items:
            if live(h):
                c=h.split("#")[0]==page and "#" not in h; cur|=c
                li.append(f'<li><a href="{h}"{" aria-current=\"page\"" if c else ""}><b>{e(t)}</b><small>{e(d)}</small></a></li>')
            else: li.append(f'<li><span class="soon" aria-disabled="true"><b>{e(t)}<em>In preparation</em></b><small>{e(d)}</small></span></li>')
        out.append(f'<li class="g{" cur" if cur else ""}"><button class="gb" type="button" aria-expanded="false" aria-controls="m-{k}">{e(name)}</button><div class="fly" id="m-{k}" role="group" aria-label="{e(lab)}"><p class="lb">{e(lab)}</p><p class="fd">{e(desc)}</p><ul>{"".join(li)}</ul></div></li>')
    return ('<header>\n<a href="index.html" aria-label="Blackvault home"><img src="assets/logo-lockup.svg" alt="Blackvault" width="170" height="30"></a>\n'
     '<button class="mb" type="button" aria-expanded="false">MENU</button>\n<nav aria-label="Primary"><ul>\n'+"\n".join(out)+'\n</ul></nav>\n'
     '<div class="rail-ft">Group in formation<br><a href="mailto:enquiries@blackvault.co.ke" data-mail="general"><span>enquiries@blackvault.co.ke</span></a></div>\n</header>')
for f in sorted(glob.glob(os.path.join(ROOT,"*.html"))):
    s=open(f,encoding="utf-8").read(); n=re.sub(r"<header>.*?</header>",lambda m:header(os.path.basename(f)),s,count=1,flags=re.S)
    open(f,"w",encoding="utf-8").write(n); print("nav ->",os.path.basename(f))
for k,name,lab,d,items in MENU:
    for t,_,h in items:
        if not live(h): print("  in preparation:",t)
