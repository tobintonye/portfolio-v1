"""
Structured content for each project's case-study page.

Kept as a plain dict (rather than DB models) since this is static portfolio
content that changes only when Tonye ships a new project. Each entry drives
the same project_detail.html template via portfolioapp.views.project_detail.
"""

PROJECTS = {

    "echoslot": {
        "title": "EchoSlot",
        "subtitle": "Appointment Scheduling App",
        "type": "Web Application",
        "type_icon": "fa-solid fa-calendar-check",
        "tagline": "A full-stack scheduling platform that lets clients book real time slots "
                    "with service providers, with zero double-bookings.",
        "github": "https://github.com/tobintonye/echoslot",
        "live": None,
        "live_note": "The live demo is currently offline continuous hosting for a full "
                      "Django + MySQL stack wasn't worth the monthly cost for a portfolio "
                      "project. The full source, including the booking and availability "
                      "logic, is on GitHub.",
        "overview": (
            "EchoSlot is a full-stack appointment scheduling application built with Django. "
            "Clients and service providers get separate role-based dashboards from a single "
            "user model: providers define services and weekly availability, clients browse "
            "open slots and book them. The booking flow is exposed twice once as a "
            "server-rendered HTMX form for the web app, and once as a Django REST Framework "
            "endpoint (documented with drf-yasg/Swagger) both backed by the same "
            "availability engine so the two surfaces can never disagree about what's open."
        ),
        "architecture_summary": (
            "Three Django apps split the concerns cleanly: accounts handles auth and roles, "
            "serviceapp owns providers, services, and the availability/booking engine, and "
            "clientapp renders the client-facing booking UI. Both the HTMX views and the DRF "
            "API sit on top of the same serviceapp logic layer."
        ),
        "diagrams": [
            {
                "title": "Booking Request Flow",
                "nodes": [
                    {"icon": "fa-solid fa-desktop", "label": "Client Browser"},
                    {"icon": "fa-solid fa-server", "label": "HTMX View / DRF Endpoint"},
                    {"icon": "fa-solid fa-calendar-check", "label": "Availability Engine"},
                    {"icon": "fa-solid fa-database", "label": "MySQL (Appointments)"},
                    {"icon": "fa-solid fa-envelope", "label": "Email Notification"},
                ],
            },
        ],
        "highlights": [
            "Built a slot-availability engine that cross-references a provider's weekly "
            "AvailabilitySchedule against already-booked Appointments to compute genuinely "
            "open slots over a rolling 30-day window, instead of trusting the frontend.",
            "Wrapped booking writes in transaction.atomic() so an appointment record and its "
            "provider/client notification emails commit or roll back together, "
            "preventing half-created bookings.",
            "Exposed the same booking flow through both a server-rendered HTMX form and a "
            "Django REST Framework endpoint (documented with drf-yasg) sharing one "
            "availability/conflict-check code path, so web and API clients can't drift apart.",
            "Role-based dashboards (client vs. service provider) driven off a single "
            "extended user model rather than separate app silos.",
        ],
        "stack_layers": {
            "Backend": "Python, Django, Django REST Framework",
            "Frontend": "Django Templates, HTMX, CSS",
            "Database": "MySQL",
            "Docs": "drf-yasg (Swagger / OpenAPI)",
        },
        "tech_stack": ["Python", "Django", "Django REST Framework", "HTMX", "MySQL"],
    },

    "vaultapp": {
        "title": "Vaultapp",
        "subtitle": "Authentication & Authorization System",
        "type": "Security & Auth",
        "type_icon": "fa-solid fa-lock",
        "tagline": "A production-style Spring Boot auth backend with JWT, refresh tokens, "
                   "and Google OAuth2 account linking.",
        "github": "https://github.com/tobintonye/Vaultapp",
        "live": None,
        "live_note": None,
        "overview": (
            "Vaultapp is a standalone authentication and authorization backend built with "
            "Spring Boot and Spring Security, designed to be dropped in front of a React, "
            "Vue, or mobile frontend. It supports email/password login and Google OAuth2 "
            "login side by side, issuing short-lived JWT access tokens plus longer-lived "
            "refresh tokens for session renewal."
        ),
        "architecture_summary": (
            "A classic layered Spring Boot architecture Controller, Service, Repository "
            "(JPA/Hibernate) sits behind a Spring Security filter chain. A custom JWT "
            "filter validates bearer tokens on every request, while a separate OAuth2 path "
            "(CustomOAuth2UserService + OAuth2SuccessHandler) handles the Google login "
            "handshake and hands off to the same token-issuing service."
        ),
        "diagrams": [
            {
                "title": "Email/Password Login",
                "nodes": [
                    {"icon": "fa-solid fa-desktop", "label": "Client"},
                    {"icon": "fa-solid fa-shield-halved", "label": "Spring Security Filter Chain"},
                    {"icon": "fa-solid fa-server", "label": "Auth Controller"},
                    {"icon": "fa-solid fa-database", "label": "User & Refresh Token DB"},
                    {"icon": "fa-solid fa-key", "label": "JWT + Refresh Token"},
                ],
            },
            {
                "title": "Google OAuth2 Login",
                "nodes": [
                    {"icon": "fa-solid fa-desktop", "label": "Client"},
                    {"icon": "fa-brands fa-google", "label": "Google OAuth2 Consent"},
                    {"icon": "fa-solid fa-server", "label": "CustomOAuth2UserService"},
                    {"icon": "fa-solid fa-user-check", "label": "Link or Create Account"},
                    {"icon": "fa-solid fa-key", "label": "OAuth2SuccessHandler issues JWT"},
                ],
            },
        ],
        "highlights": [
            "Issues stateless JWT access tokens paired with persisted, rotating refresh "
            "tokens, so sessions can be renewed without forcing a re-login.",
            "A custom CustomOAuth2UserService reconciles a Google identity against existing "
            "local accounts by email linking to an existing user instead of silently "
            "creating a duplicate account for the same person.",
            "Provider-aware user model (LOCAL vs. GOOGLE) keeps password-based and "
            "OAuth-based identities in one table without conflating their auth methods.",
            "Tracks failed login attempts per account as a basic brute-force / lockout "
            "safeguard, ahead of full rate-limiting.",
        ],
        "stack_layers": {
            "Backend": "Java, Spring Boot, Spring Security",
            "Auth": "JWT, OAuth2 Client (Google)",
            "Persistence": "JPA / Hibernate, MySQL / PostgreSQL",
            "Build": "Maven",
        },
        "tech_stack": ["Java", "Spring Boot", "Spring Security", "OAuth2", "JWT", "PostgreSQL"],
    },

    "estore": {
        "title": "eStore",
        "subtitle": "E-Commerce REST API",
        "type": "API Development",
        "type_icon": "fa-solid fa-server",
        "tagline": "A modular Spring Boot commerce API covering products, carts, orders, "
                   "and real Paystack payments.",
        "github": "https://github.com/tobintonye/estore",
        "live": None,
        "live_note": None,
        "overview": (
            "eStore is a RESTful e-commerce backend split into independent Spring Boot "
            "modules accounts, storeapp (products), cartapp, orderapp, and payments each "
            "with its own controller, service, repository, and DTOs. Product images are "
            "handled through Cloudinary rather than local disk storage, and checkout is wired "
            "to Paystack for real payment processing."
        ),
        "architecture_summary": (
            "Each domain module follows the same Controller → Service → Repository shape, "
            "with DTOs at the boundary so internal JPA entities are never serialized "
            "directly to clients. The payments module talks to Paystack through a reactive "
            "WebClient, keeping the order record not the incoming request as the single "
            "source of truth for what's actually owed."
        ),
        "diagrams": [
            {
                "title": "Order & Payment Flow",
                "nodes": [
                    {"icon": "fa-solid fa-desktop", "label": "Client"},
                    {"icon": "fa-solid fa-cart-shopping", "label": "Cart / Order Controller"},
                    {"icon": "fa-solid fa-database", "label": "Order (MySQL)"},
                    {"icon": "fa-solid fa-credit-card", "label": "PaymentService"},
                    {"icon": "fa-solid fa-cloud", "label": "Paystack (WebClient)"},
                    {"icon": "fa-solid fa-circle-check", "label": "Verify & Mark Paid"},
                ],
            },
        ],
        "highlights": [
            "Payment amount is read from the Order row itself and converted to kobo before "
            "calling Paystack's initialize endpoint the client can influence which order "
            "gets paid, but never how much it costs.",
            "Verification calls Paystack's own /transaction/verify endpoint and checks its "
            "response before marking an order PAID, rather than trusting a client-side "
            "'payment succeeded' flag.",
            "Guards against double-charging by rejecting a new payment attempt if the order "
            "is already in PAID status.",
            "Product images go through a dedicated ImageUploadService backed by Cloudinary, "
            "keeping media storage out of the application server entirely.",
            "DTOs (request/response) at every controller boundary keep JPA entities from "
            "leaking into the API contract.",
        ],
        "stack_layers": {
            "Backend": "Java 21, Spring Boot, Spring Data JPA",
            "Security": "Spring Security, JWT",
            "Payments": "Paystack API (reactive WebClient)",
            "Media": "Cloudinary",
            "Database": "MySQL",
        },
        "tech_stack": ["Java", "Spring Boot", "MySQL", "Paystack", "Cloudinary"],
    },

    "easetalk": {
        "title": "EaseTalk",
        "subtitle": "Anonymous Support Platform",
        "type": "Real-Time App",
        "type_icon": "fa-solid fa-comments",
        "tagline": "A privacy-first, real-time messaging platform connecting anonymous "
                   "users with service providers over WebSockets.",
        "github": "https://github.com/tobintonye/Anonymous-Therapy-app",
        "live": None,
        "live_note": "Built as a learning/portfolio project to explore real-time "
                      "architecture and privacy-first design — not for real-world "
                      "therapy or healthcare use.",
        "overview": (
            "EaseTalk lets a user sign up without providing any identifying information — "
            "the backend auto-generates an anonymous username — and message a service "
            "provider privately and in real time. It's built on Django Channels rather than "
            "plain HTTP polling, so messages arrive instantly over a persistent WebSocket "
            "connection."
        ),
        "architecture_summary": (
            "A custom user model auto-assigns a random anon_xxxxxxxx username to any user "
            "who signs up under the anonymousUser role, so no real name ever touches the "
            "database. Real-time delivery runs through an ASGI ChannelConsumer with a "
            "Redis-backed channel layer, using a deterministic room name built from the two "
            "participants' sorted user IDs so both sides always land in the same room."
        ),
        "diagrams": [
            {
                "title": "Real-Time Message Flow",
                "nodes": [
                    {"icon": "fa-solid fa-desktop", "label": "Browser (WebSocket)"},
                    {"icon": "fa-solid fa-bolt", "label": "ASGI ChatConsumer"},
                    {"icon": "fa-solid fa-layer-group", "label": "Redis Channel Layer"},
                    {"icon": "fa-solid fa-comments", "label": "Room Group Broadcast"},
                    {"icon": "fa-solid fa-database", "label": "MySQL (Message Log)"},
                ],
            },
        ],
        "highlights": [
            "Custom CustomUserManager auto-generates an 8-character anonymous username at "
            "account creation for the anonymousUser role, so anonymity is enforced at the "
            "model layer, not just hidden in the UI.",
            "Chat rooms are named deterministically from the two participants' sorted user "
            "IDs, so both the sender's and receiver's WebSocket connections always resolve "
            "to the same Channels group without a separate room-lookup table.",
            "Runs on a Redis-backed Channel Layer rather than the in-memory default, so "
            "message broadcasting works correctly across multiple ASGI worker processes.",
            "Every message is still persisted to the database from within the async "
            "consumer (via sync_to_async), so the real-time layer doesn't come at the cost "
            "of a durable message history.",
            "Three-tier role system (anonymousUser / therapist / admin) built directly into "
            "a single custom user model rather than bolted on with a separate profile table.",
        ],
        "stack_layers": {
            "Backend": "Python, Django, Django Channels",
            "Real-time": "ASGI, WebSockets, Redis Channel Layer",
            "Frontend": "HTML, CSS, JavaScript",
            "Database": "MySQL",
        },
        "tech_stack": ["Python", "Django", "Django Channels", "WebSockets", "Redis", "MySQL"],
    },
}
