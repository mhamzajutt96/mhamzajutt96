<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/header-dark.svg">
  <img alt="Muhammad Hamza — Senior Software Engineer, Ruby on Rails" src="./assets/header-light.svg" width="100%">
</picture>

I build production Rails systems that handle money, file taxes, and keep working
when the internet doesn't — and I run one of them as a business.

- **Senior Backend Engineer at [UMAI](https://umai.io)** — reservation software for restaurants; the reservation call flow, waitlists and queue management.
- **Founder and sole engineer of [Hajza](https://hajza.com)** — booking and point-of-sale, live with paying venues in Pakistan and the UAE.

<br>

### Previously

| | | |
|---|---|---|
| **2022 – 2025** | Senior Software Developer | K&W Media Consulting, Hamburg *(contract)* |
| **2022** | Senior Software Engineer | Dubizzle Labs (EMPG), Lahore |
| **2020 – 2021** | Senior Software Engineer | Tiksom Limited, Lahore |
| **2018 – 2020** | Associate Software Engineer | System Plus, Lahore |

<br>

## Hajza · [hajza.com](https://hajza.com)

A multi-tenant Rails 8 platform: bookings, staff and payroll, inventory,
a public storefront, government tax filing, and a till that keeps selling
when the network drops. 94 tables, one codebase, and no `default_scope`
anywhere — every query scopes itself.

I designed it, built it, deploy it and answer the support calls.

**The parts that were actually hard:**

**Tenant isolation, enforced by the model layer.** Scoping every read is necessary
and not sufficient — a form that saves a submitted `*_id` without looking it up
through the current tenant writes a cross-tenant link, and the correctly scoped
read then displays it. Writes are validated against the tenant of every record
they link to, derived from each model's own associations, so a new association is
covered the day it is added rather than the day someone remembers it.

**Live government e-invoicing.** Every sale is filed with Pakistan's Punjab Revenue
Authority as a real fiscal invoice; voids file credit notes against it. The job
claims its row *before* the request goes out, because the success branch is skipped
exactly when the outcome is uncertain — which is the case the guard exists for.

**An offline-first POS.** IndexedDB outbox, service worker, background sync. A sale
taken offline is the only record of that sale, so it is deleted locally on a genuine
`2xx` and nothing else — a session that expired mid-shift answers a queued `POST`
with a redirect to a login page, which is a `200` if you only ask `res.ok`.

**Client money that agrees with the server, to the cent.** The browser's total mirrors
the server's tax calculation exactly, as a pure module compared against Rails over 288
generated bills — two venues, three tax modes, fees, discounts, tips. Unrounded, 178
of them disagreed by half a cent, which becomes a whole cent in the amount field and
a payment the server refuses.

**Records that were counted stay counted.** Closed shifts freeze the fee rates they
were reconciled at, rather than re-deriving them from settings someone can edit today.
A payment the tax authority has accepted is corrected by a new entry, never by
rewriting the old one.

<br>

## How I work

- **Every behaviour change ships with a test**, and a regression test is only evidence once I've watched it fail against the old code.
- **The failure gets written down.** Every convention in that codebase names the bug that caused it, so the next person can judge whether their case is genuinely different.
- **Verify the artifact, not the workspace.** The working tree, the index and the branch are three different objects, and they diverge quietly.

<br>

## Stack

| | |
|---|---|
| **Core** | Ruby 3.4 · Rails 8.1 · PostgreSQL 16 · Hotwire (Turbo + Stimulus) · Tailwind CSS |
| **Background** | Solid Queue · Solid Cache · Solid Cable — no Redis in the stack |
| **Frontend** | ES modules · importmap · IndexedDB · service workers · Propshaft |
| **Infra** | Docker · Kamal · Hetzner · Cloudflare (R2, DNS, WAF) · GitHub Actions |
| **Operations** | Sentry · New Relic · Rack::Attack · SimpleCov behind a ratcheted CI floor |

<br>

## A note on the graph below

Most of what I build is private — client platforms and my own product. The public
repository count here is not the interesting number; the contribution graph is the
honest one.

<br>

---

<div align="center">

**[hajza.com](https://hajza.com)** · **[LinkedIn](https://www.linkedin.com/in/mhamzajutt96/)** · **[mhamzajutt96@gmail.com](mailto:mhamzajutt96@gmail.com)**

</div>
