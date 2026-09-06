# Sinavaland

Tourism platform built with Django.

## Overview

Sinavaland is a multi-module web application designed for the tourism sector. The platform provides functionality for managing accommodations, tours, a marketplace, and content (magazine), along with user accounts and subscription features.

The project focuses on modular architecture, flexible content management, and a production-ready configuration structure.

## Key Features

- Accommodation listing and management
- Tour management system
- Marketplace module
- Content/magazine section
- Custom user model with subscription support (golden membership)
- Progressive Web App (PWA) capabilities
- Media handling and static file management
- Environment-based configuration for different environments

## Technical Highlights

- Multi-app architecture with clear separation of concerns
- Custom user model with extended profile and subscription fields
- Flexible database configuration (SQLite / MySQL)
- Media and static file handling suitable for production
- PWA integration for improved mobile experience
- Clean URL structure and modular routing
- Use of environment variables for secure configuration

## Tech Stack

- **Backend:** Python, Django
- **Database:** MySQL / SQLite
- **Frontend:** Django Templates, HTML, CSS, JavaScript
- **Other:** django-pwa, Pillow, python-decouple

## Project Structure


Sinavaland/
├── accounts/          # Custom user model and authentication
├── accommodations/    # Accommodation management
├── tours/             # Tour management
├── marketplace/       # Marketplace functionality
├── magazine/          # Content and magazine section
├── core/              # Shared functionality
├── sinavaland/        # Project settings and configuration
└── manage.py


## Purpose

This project demonstrates the ability to design and implement a multi-module Django application with real-world domain requirements, modular structure, and production-oriented setup — relevant for corporate full-stack and backend development roles.
