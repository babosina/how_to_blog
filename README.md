# How To Blog

Disclaimer. The project is intended as a learning curve of web development with Python from a QA perspective. It doesn't aim to be a hands-on application. This web application allows users to view blog posts, read about the author, and send messages through a contact form.

## Features

- Responsive design for all devices ([Bootstrap](https://getbootstrap.com/))
- Dynamic blog posts loaded from an external API ([Npoint](https://www.npoint.io/))
- Individual post pages with detailed content
- About page with author information
- Contact form with email notification functionality

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd how_to_blog
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables by creating a `.env` file in the project root with the following variables:
   ```
   MY_EMAIL=your-email@example.com
   MY_PASSWORD=your-email-password
   SMTP_SERVER=your-smtp-server (e.g., smtp.gmail.com)
   SECRET_KEY=your-flask-secret-key
   ```

## Usage

1. Run the application:
   ```
   python main.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Project Structure

```
how_to_blog/
├── main.py                 # Main application file
├── README.md               # Project documentation
├── static/                 # Static assets
│   ├── assets/             # Images and favicon
│   ├── css/                # CSS stylesheets
│   └── js/                 # JavaScript files
└── templates/              # HTML templates
    ├── about.html          # About page template
    ├── contact.html        # Contact page template
    ├── footer.html         # Footer template
    ├── header.html         # Header template
    ├── index.html          # Home page template
    └── post.html           # Individual post template
```

## Dependencies

- Flask: Web framework
- Requests: HTTP library for API calls
- python-dotenv: Environment variable management
- smtplib: Email functionality

## API Integration - DEPRECATED

The blog posts are fetched from an external API endpoint. The application uses the following endpoint:
```
https://api.npoint.io/405401fd224c5d58a066
```

## Database Integration
A simple local SQL DB (SQLite) is created to store all posts

## License

This project is not licensed.

## Contributing

Contributions are welcome but not required at all😜