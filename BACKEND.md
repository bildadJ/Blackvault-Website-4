# Blackvault: what is static and what needs a backend

Everything in this project runs as static files on Cloudflare Pages. Nothing here simulates a login, a submission or a verification. Items below need configuration.

| Feature | Needs | Recommended setup |
|---|---|---|
| Public pages, research library, publications list | Static only | Edit HTML (or generate from Markdown/JSON); push to GitHub |
| Contact form | Third-party service | Create a Formspree form, paste its URL into `FORM_ENDPOINT` in `assets/main.js` (already allowed by `_headers`) |
| Opportunity / proposal submissions with documents | Server + storage | Pages Function or Worker, Turnstile (spam check), R2 (files), D1 (records), email notification. `submit.html` is live and sends text by email (or Formspree); file upload is the part still to build |
| Document verification | Database + server | D1 table of issued reference numbers and file hashes; Worker endpoint `/api/verify`; add the reference to each official PDF. Not yet built |
| Partner Portal (`partner-area.html`) | Authentication | Cloudflare Zero Trust > Access > self-hosted application on `blackvault.co.ke/partner-area*`; policy: email one-time PIN for an approved list |
| Officials Portal (`officials-area.html`) | Authentication | Separate Access application on `/officials-area*` with its own stricter policy (named emails or company identity provider, MFA) |
| Blackvault Briefing newsletter | Email service | Use a provider (Buttondown, MailerLite or Brevo) with double opt-in; link its hosted form. `briefing.html` currently collects interest by email only |
| Multilingual | Content work | Static copies per language (`/sw/…`) with `hreflang`; translate by a person, not an in-browser widget. Start with English and Swahili for key pages |

## Important: activate access control before adding any portal content
The two `*-area.html` pages are public files until Cloudflare Access is configured. They contain no information. Do not put any partner or official content in them, or in any file in this repository, because a public GitHub repository and a public site both expose it. Real portal content must come from a protected backend after Access is active.

## Deployment
1. Push the folder to GitHub. 2. Cloudflare Pages: connect the repo, no build command, output directory `/`. 3. Set up the custom domain. 4. Configure Access applications. 5. Add the Formspree URL.

## Maintaining the site
Edit the menu in `tools/build-nav.py`, and sector, research and portal pages in `tools/build-pages.py`. Run `python3 tools/build-pages.py && python3 tools/build-nav.py`. Pages you edit by hand (home, Agri Ventures, Technology, Governance, Capital, Research, Publications) are not overwritten except for their header.
