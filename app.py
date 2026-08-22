from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):

        message = """
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>Deepak Sagar | Docker CI/CD</title>

    <style>

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: Arial, Helvetica, sans-serif;
            background: #0f172a;
            color: white;
            line-height: 1.6;
        }

        /* NAVBAR */

        nav {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 70px;

            display: flex;
            align-items: center;
            justify-content: space-between;

            padding: 0 8%;

            background: rgba(15, 23, 42, 0.92);
            backdrop-filter: blur(10px);

            border-bottom: 1px solid rgba(255,255,255,0.1);

            z-index: 1000;
        }

        .logo {
            font-size: 24px;
            font-weight: bold;
        }

        .logo span {
            color: #38bdf8;
        }

        nav ul {
            display: flex;
            gap: 30px;
            list-style: none;
        }

        nav a {
            color: #cbd5e1;
            text-decoration: none;
            font-size: 15px;
            transition: 0.3s;
        }

        nav a:hover {
            color: #38bdf8;
        }

        /* HERO */

        .hero {
            min-height: 100vh;

            display: flex;
            align-items: center;
            justify-content: center;

            text-align: center;

            padding: 120px 20px 80px;

            background:
                radial-gradient(
                    circle at top left,
                    #1e40af 0%,
                    transparent 35%
                ),
                radial-gradient(
                    circle at bottom right,
                    #0e7490 0%,
                    transparent 35%
                ),
                #0f172a;
        }

        .hero-content {
            max-width: 900px;
        }

        .badge {
            display: inline-block;

            padding: 8px 18px;

            border: 1px solid #38bdf8;

            border-radius: 30px;

            color: #38bdf8;

            font-size: 14px;

            margin-bottom: 25px;
        }

        .hero h1 {
            font-size: clamp(45px, 7vw, 80px);

            line-height: 1.1;

            margin-bottom: 25px;
        }

        .hero h1 span {
            color: #38bdf8;
        }

        .hero p {
            max-width: 700px;

            margin: auto;

            color: #cbd5e1;

            font-size: 19px;

            margin-bottom: 40px;
        }

        .buttons {
            display: flex;

            justify-content: center;

            gap: 15px;

            flex-wrap: wrap;
        }

        .btn {
            padding: 14px 28px;

            border-radius: 8px;

            text-decoration: none;

            font-weight: bold;

            transition: 0.3s;
        }

        .btn-primary {
            background: #38bdf8;

            color: #082f49;
        }

        .btn-primary:hover {
            transform: translateY(-3px);

            background: #7dd3fc;
        }

        .btn-secondary {
            border: 1px solid #475569;

            color: white;
        }

        .btn-secondary:hover {
            border-color: #38bdf8;

            color: #38bdf8;
        }

        /* TECHNOLOGY SECTION */

        section {
            padding: 100px 8%;
        }

        .section-title {
            text-align: center;

            margin-bottom: 50px;
        }

        .section-title h2 {
            font-size: 42px;

            margin-bottom: 10px;
        }

        .section-title p {
            color: #94a3b8;
        }

        .cards {
            display: grid;

            grid-template-columns:
                repeat(auto-fit, minmax(220px, 1fr));

            gap: 25px;

            max-width: 1100px;

            margin: auto;
        }

        .card {
            padding: 30px;

            background: #1e293b;

            border: 1px solid #334155;

            border-radius: 15px;

            transition: 0.3s;
        }

        .card:hover {
            transform: translateY(-8px);

            border-color: #38bdf8;

            box-shadow:
                0 15px 40px rgba(0,0,0,0.3);
        }

        .icon {
            font-size: 40px;

            margin-bottom: 20px;
        }

        .card h3 {
            margin-bottom: 10px;

            font-size: 22px;
        }

        .card p {
            color: #94a3b8;

            font-size: 15px;
        }

        /* PIPELINE */

        .pipeline {
            max-width: 1100px;

            margin: auto;

            display: flex;

            align-items: center;

            justify-content: center;

            flex-wrap: wrap;

            gap: 15px;
        }

        .pipeline-item {
            padding: 20px;

            min-width: 140px;

            text-align: center;

            background: #1e293b;

            border: 1px solid #334155;

            border-radius: 12px;
        }

        .pipeline-item strong {
            display: block;

            margin-top: 8px;

            color: #38bdf8;
        }

        .arrow {
            font-size: 28px;

            color: #38bdf8;
        }

        /* STATUS */

        .status-section {
            background: #020617;

            text-align: center;
        }

        .status {
            display: inline-flex;

            align-items: center;

            gap: 10px;

            padding: 12px 22px;

            border-radius: 30px;

            background: rgba(34,197,94,0.1);

            border: 1px solid #22c55e;

            color: #4ade80;
        }

        .dot {
            width: 10px;

            height: 10px;

            background: #22c55e;

            border-radius: 50%;

            box-shadow: 0 0 10px #22c55e;
        }

        /* FOOTER */

        footer {
            padding: 30px;

            text-align: center;

            color: #64748b;

            border-top: 1px solid #1e293b;
        }

        footer span {
            color: #38bdf8;
        }

        /* MOBILE */

        @media (max-width: 700px) {

            nav {
                padding: 0 5%;
            }

            nav ul {
                display: none;
            }

            .hero {
                padding-top: 110px;
            }

            section {
                padding: 70px 5%;
            }

            .hero p {
                font-size: 16px;
            }

            .section-title h2 {
                font-size: 32px;
            }

            .arrow {
                transform: rotate(90deg);
            }
        }

    </style>

</head>


<body>


<!-- NAVBAR -->

<nav>

    <div class="logo">
        Deepak<span>Sagar</span>
    </div>

    <ul>

        <li>
            <a href="#home">Home</a>
        </li>

        <li>
            <a href="#technologies">Technologies</a>
        </li>

        <li>
            <a href="#pipeline">Pipeline</a>
        </li>

        <li>
            <a href="#status">Status</a>
        </li>

    </ul>

</nav>


<!-- HERO -->

<section class="hero" id="home">

    <div class="hero-content">

        <div class="badge">
            🚀 Automated DevOps Deployment
        </div>

        <h1>
            Build. Ship.
            <span>Deploy.</span>
        </h1>

        <p>
            Welcome to my automated Docker CI/CD project.
            This application is built with Python, containerized
            using Docker, pushed through Docker Hub and
            automatically deployed to an AWS EC2 instance
            using GitHub Actions.
        </p>

        <div class="buttons">

            <a href="#pipeline"
               class="btn btn-primary">
                View Pipeline
            </a>

            <a href="#technologies"
               class="btn btn-secondary">
                Technologies
            </a>

        </div>

    </div>

</section>


<!-- TECHNOLOGIES -->

<section id="technologies">

    <div class="section-title">

        <h2>Technologies</h2>

        <p>
            Tools used to build and deploy this application
        </p>

    </div>


    <div class="cards">


        <div class="card">

            <div class="icon">🐍</div>

            <h3>Python</h3>

            <p>
                Lightweight HTTP server used to serve
                this web application.
            </p>

        </div>


        <div class="card">

            <div class="icon">🐳</div>

            <h3>Docker</h3>

            <p>
                The application is packaged and deployed
                inside a Docker container.
            </p>

        </div>


        <div class="card">

            <div class="icon">⚙️</div>

            <h3>GitHub Actions</h3>

            <p>
                Automates the build, push and deployment
                process whenever code is updated.
            </p>

        </div>


        <div class="card">

            <div class="icon">☁️</div>

            <h3>AWS EC2</h3>

            <p>
                The Docker container runs on an AWS EC2
                Ubuntu server.
            </p>

        </div>


    </div>

</section>


<!-- PIPELINE -->

<section id="pipeline">

    <div class="section-title">

        <h2>CI/CD Pipeline</h2>

        <p>
            From code commit to production deployment
        </p>

    </div>


    <div class="pipeline">


        <div class="pipeline-item">

            💻

            <strong>GitHub</strong>

            <small>
                Code Push
            </small>

        </div>


        <div class="arrow">
            →
        </div>


        <div class="pipeline-item">

            ⚙️

            <strong>Actions</strong>

            <small>
                Automation
            </small>

        </div>


        <div class="arrow">
            →
        </div>


        <div class="pipeline-item">

            🐳

            <strong>Docker</strong>

            <small>
                Build Image
            </small>

        </div>


        <div class="arrow">
            →
        </div>


        <div class="pipeline-item">

            📦

            <strong>Docker Hub</strong>

            <small>
                Store Image
            </small>

        </div>


        <div class="arrow">
            →
        </div>


        <div class="pipeline-item">

            ☁️

            <strong>AWS EC2</strong>

            <small>
                Deploy
            </small>

        </div>


    </div>

</section>


<!-- STATUS -->

<section class="status-section"
         id="status">

    <div class="section-title">

        <h2>Application Status</h2>

        <p>
            Current deployment status
        </p>

    </div>


    <div class="status">

        <div class="dot"></div>

        Application Running

    </div>

</section>


<!-- FOOTER -->

<footer>

    <p>
        Built with ❤️ by
        <span>Deepak Sagar</span>
    </p>

    <p>
        Docker • GitHub Actions • Docker Hub • AWS EC2
    </p>

</footer>


</body>

</html>
"""

        self.send_response(200)

        self.send_header(
            "Content-type",
            "text/html"
        )

        self.send_header(
            "Content-Length",
            str(len(message.encode()))
        )

        self.end_headers()

        self.wfile.write(
            message.encode()
        )


server = HTTPServer(
    ("0.0.0.0", 5000),
    Handler
)

print("Server running on port 5000")

server.serve_forever()