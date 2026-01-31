# ClinOva - Nursing Practical Assessment App

**Backend API for a Nursing Practical Assessment Application**

ClinOva is a comprehensive Django REST Framework-based backend system designed to streamline and digitize practical assessments at nursing training colleges. The platform enables efficient evaluation of nursing students' procedural competencies through a structured, multi-examiner assessment process with reconciliation workflows.

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Management Commands](#management-commands)
- [User Roles](#user-roles)
- [Data Models](#data-models)
- [Development Notes](#development-notes)

---

## Overview

ClinOva addresses the challenges of traditional paper-based nursing practical assessments by providing:

- **Digital Assessment Platform**: Replace manual grading sheets with a modern, digital interface
- **Multi-Examiner Workflow**: Support simultaneous assessment by two independent examiners with built-in reconciliation
- **Procedural Tracking**: Organize and score individual steps within complex nursing procedures
- **Data Management**: Import/export student and procedure data efficiently
- **Reconciliation System**: Manage discrepancies between examiner scores through a dedicated reconciliation process
- **Student Programs**: Support multiple nursing programs (e.g., RN, PN) with level-based organization (100-400 levels)

---

## Key Features

### Core Functionality

- **Student Management**: Track nursing students by program, level, and index number
- **Procedure Library**: Define nursing procedures with detailed steps and scoring criteria
- **Dual Examiner Assessment**: Assign two examiners per procedure to ensure objective evaluation
- **Step-Based Scoring**: Score individual procedure steps rather than entire procedures
- **Reconciliation Workflow**: Compare examiner scores and resolve discrepancies
- **Care Plan Tracking**: Document care plans associated with student procedures
- **Role-Based Access**: Admin and Examiner roles with appropriate permissions

### Data Management

- **Bulk Import/Export**: Import student and procedure data via Excel/CSV templates
- **Data Export Formats**: Export assessment data as CSV, Excel, or PDF reports
- **Template Generation**: Auto-generate import templates for consistent data formatting
- **Complete Data Backup**: Export and import entire datasets for backup/migration

---

## Tech Stack

### Backend Framework
- **Django 4.2.16**: Python web framework
- **Django REST Framework 3.16.0**: REST API toolkit
- **Django CORS Headers 4.7.0**: Cross-Origin Resource Sharing support

### Authentication & Authorization
- **Simple JWT 5.5.0**: JWT token-based authentication
- **Django built-in**: User authentication and permissions

### Database
- **SQLite3** (Development): Default database
- **MySQL** (Optional): Configure via environment variables
- **PostgreSQL** (Optional): Configure via environment variables

### Data Processing & Export
- **openpyxl 3.1.5**: Excel file handling
- **reportlab 4.4.7**: PDF generation
- **django-import-export 4.3.14**: Data import/export utilities
- **tablib 3.9.0**: Tabular data handling
- **python-dotenv 1.1.0**: Environment variable management

### Database Drivers
- **mysqlclient 2.2.7**: MySQL Python adapter
- **psycopg2-binary 2.9.10**: PostgreSQL Python adapter


---

## Project Structure

```
d:/Nursing Practical App Backend/
├── manage.py                          # Django management script
├── requirements.txt                   # Python dependencies
├── db.sqlite3                         # SQLite database
├── README.md                          # This file
│
├── nursing_practical/                 # Project configuration
│   ├── settings.py                    # Django settings
│   ├── urls.py                        # Main URL router
│   ├── wsgi.py                        # WSGI configuration
│   └── asgi.py                        # ASGI configuration
│
├── accounts/                          # User authentication app
│   ├── models.py                      # User model (extends AbstractUser)
│   ├── views.py                       # Authentication views (Login, Logout, etc.)
│   ├── serializers.py                 # User serializers
│   ├── urls.py                        # Authentication endpoints
│   ├── admin.py                       # Admin configuration
│   └── migrations/                    # Database migrations
│
├── exams/                             # Assessment app (core)
│   ├── models.py                      # Data models (Program, Student, Procedure, etc.)
│   ├── views.py                       # API views for assessment
│   ├── serializers.py                 # Model serializers
│   ├── urls.py                        # Assessment endpoints
│   ├── admin.py                       # Admin configuration
│   ├── management/
│   │   └── commands/                  # Custom management commands
│   │       ├── create_import_template.py       # Generate import templates
│   │       ├── import_data.py                  # Bulk import data
│   │       ├── import_complete_data.py         # Full dataset import
│   │       ├── export_all_data.py              # Export all data
│   │       └── export_complete_data.py         # Full dataset export
│   └── migrations/                    # Database migrations
│
└── static/                            # Static files directory
```

---

## Installation

### Prerequisites

- **Python 3.8+**
- **pip** (Python package manager)
- **Git**
- **Virtual Environment** (recommended)

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd "Nursing Practical App Backend"
```

### Step 2: Create Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

### Environment Variables

Create a `.env` file in the project root directory:

```env
# Django Security
DJANGO_SECRET_KEY=your-secret-key-here

# Database Configuration
DB_ENGINE=django.db.backends.sqlite3
# Alternatively for MySQL:
# DB_ENGINE=django.db.backends.mysql
# DB_NAME=nursing_practical
# DB_USER=root
# DB_PASSWORD=password
# DB_HOST=localhost
# DB_PORT=3306

# Allowed Hosts
BACKEND_URL=example.com
BACKEND_DEV_URL=127.0.0.1:8000
FRONTEND_URL=https://example.com
FRONTEND_DEV_URL=http://localhost:3000
LOCALHOST=127.0.0.1
```

### Generate Django Secret Key

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

---

## Database Setup

### Step 1: Create Migrations

```bash
python manage.py makemigrations
```

### Step 2: Apply Migrations

```bash
python manage.py migrate
```

### Step 3: Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

You will be prompted to enter:
- **Username**: Your admin username
- **Email**: Your email address
- **Password**: Your secure password

### Step 4: Load Initial Data (Optional)

If you have existing data in export format:

```bash
python manage.py import_complete_data <file_path>
```

---

## Running the Application

### Development Server

```bash
python manage.py runserver
```

The API will be available at: `http://127.0.0.1:8000/`

### Access Admin Panel

Navigate to: `http://127.0.0.1:8000/admin/`

Use your superuser credentials to log in.

### Production Deployment

For production deployment, use a production-grade server (Gunicorn, uWSGI) and configure proper security settings in `settings.py`.

---

## API Endpoints

### Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/accounts/login/` | User login (returns JWT tokens) |
| POST | `/api/accounts/logout/` | User logout |
| POST | `/api/accounts/change-password/` | Change user password |
| GET | `/api/accounts/examiners/` | List all examiners |

### Program Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/exams/programs/` | List all programs |
| POST | `/api/exams/programs/` | Create new program (Admin only) |

### Student Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/exams/programs/<id>/students/` | List students by program |
| POST | `/api/exams/students/` | Create new student (Admin only) |
| GET | `/api/exams/students/<id>/` | Student details |

### Procedure Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/exams/programs/<id>/procedures/` | List procedures by program |
| POST | `/api/exams/procedures/` | Create procedure (Admin only) |
| GET | `/api/exams/procedures/<id>/` | Procedure details with steps |

### Assessment Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/POST | `/api/exams/assessments/` | List or create assessments |
| PUT | `/api/exams/assessments/<id>/score/` | Score procedure steps |
| POST | `/api/exams/assessments/<id>/reconcile/` | Reconcile examiner scores |

### Dashboard Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/exams/dashboard/` | Get dashboard statistics |

---

## Management Commands

### Import/Export Data

#### Generate Import Template

```bash
python manage.py create_import_template
```

Creates CSV/Excel templates for importing students and procedures.

#### Import Student and Procedure Data

```bash
python manage.py import_data <file_path>
```

#### Complete Data Import

```bash
python manage.py import_complete_data <file_path>
```

#### Export All Data

```bash
python manage.py export_all_data
```

Exports all students, procedures, and assessment data.

#### Export Complete Data

```bash
python manage.py export_complete_data
```

Creates a backup of the entire database in exportable format.

---

## User Roles

### Admin

**Permissions:**
- Create, read, update, delete users
- Manage programs and procedures
- Import/export data
- View all assessments and reconciliations
- Access admin panel

**Typical Users:** Department coordinators, academic administrators

### Examiner

**Permissions:**
- View assigned students and procedures
- Score procedure steps during assessments
- View reconciliation requests
- Participate in score reconciliation

**Typical Users:** Faculty members, clinical instructors, assessors

---

## Data Models

### User

Extends Django's `AbstractUser` with:
- **Role**: admin or examiner
- **is_active**: User account status

### Program

- **name**: Nursing program name (e.g., "RN 3-Year", "PN")
- **abbreviation**: Short form (e.g., "RN", "PN")

### Student

- **index_number**: Unique student identifier
- **full_name**: Student full name
- **program**: Foreign key to Program
- **level**: Academic level (100, 200, 300, 400)
- **is_active**: Enrollment status

### Procedure

- **program**: Nursing procedure belongs to specific program
- **name**: Procedure name (e.g., "Catheterization", "IV Insertion")
- **total_score**: Maximum score for procedure

### ProcedureStep

- **procedure**: Parent procedure
- **description**: Step description
- **step_order**: Sequence number

### StudentProcedure

- **student**: Student being assessed
- **procedure**: Procedure being assessed
- **examiner_a**: First examiner
- **examiner_b**: Second examiner
- **status**: pending, scored, or reconciled
- **reconciled_by**: User who reconciled scores
- **assigned_reconciler**: Designated reconciler (optional)

### ProcedureStepScore

- **student_procedure**: Parent assessment
- **procedure_step**: Step being scored
- **examiner**: Scoring examiner
- **score**: Numeric score (0 or 1 for pass/fail)

### ReconciledScore

- **student_procedure**: Assessment being reconciled
- **procedure_step**: Step reconciliation
- **score**: Final reconciled score

### CarePlan

- **student**: Associated student
- **procedure**: Related procedure
- **care_plan**: Care plan documentation
- **created_at**: Creation timestamp

---

## Development Notes

### Adding New Procedures

1. Go to admin panel: `/admin/`
2. Navigate to Procedures
3. Create new procedure and add steps
4. Assign to program

### Creating Assessments Programmatically

```python
from exams.models import StudentProcedure, Student, Procedure, User

student = Student.objects.get(index_number="12345")
procedure = Procedure.objects.get(id=1)
examiner_a = User.objects.get(username="examiner1")
examiner_b = User.objects.get(username="examiner2")

assessment = StudentProcedure.objects.create(
    student=student,
    procedure=procedure,
    examiner_a=examiner_a,
    examiner_b=examiner_b
)
```

### API Response Format

All API responses follow a consistent format:

```json
{
  "status": "success",
  "data": {},
  "message": "Optional message"
}
```

### JWT Authentication

Include the JWT token in request headers:

```
Authorization: Bearer <access_token>
```

### Common Issues

1. **CORS Errors**: Ensure `CORS_ALLOWED_ORIGINS` is configured in `settings.py`
2. **Database Errors**: Run `python manage.py migrate` after schema changes
3. **Import Errors**: Verify all dependencies in `requirements.txt` are installed
4. **Authentication Failures**: Ensure user role is set to "examiner" or "admin"

---

## Future Enhancements

- [ ] Mobile app for offline assessment
- [ ] Real-time collaboration between examiners
- [ ] Advanced reporting and analytics
- [ ] Automated score reconciliation suggestions
- [ ] Email notifications for examiners
- [ ] Audit logging for all assessments

---

## License

This project is currently in development and will be made private soon.

---

## Support

For issues, questions, or contributions, please contact the development team or create an issue in the repository.
