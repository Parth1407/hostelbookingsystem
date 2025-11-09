# 🏠 Hostel Booking System

A modern, Django-based web application for managing hostel room bookings with gender-based block filtering. Built with clean design, user-friendly interface, and comprehensive booking management features.

![Django](https://img.shields.io/badge/Django-5.2.8-092E20?style=flat-square&logo=django)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite)

## ✨ Features

### 🔐 User Authentication
- **User Registration**: Create accounts with full name (first name, last name), username, email, gender, and password
- **Secure Login/Logout**: Django's built-in authentication system with custom logout handling
- **User Profile**: Display full name, gender, and booking information
- **Gender-Based Access Control**: Strict enforcement - users can only view and book rooms in blocks matching their gender

### 🏢 Block Management System
- **Block System**: Organized into gender-specific blocks
  - **Male Blocks**: B1, B2, B3
  - **Female Blocks**: G1, G2, G3
- **Block Layout Visualization**: Interactive grid-based layout showing floors and rooms for each block
- **Room Status**: Real-time availability status (Available/Booked) with color coding
- **Room Details**: Comprehensive room information including block, floor, capacity, and booking status

### 📅 Booking System
- **One Room Per User**: Users can book only one room at a time
- **Gender-Based Filtering**: Users automatically see only blocks matching their gender
- **Booking Confirmation**: Confirmation page before finalizing booking
- **Booking Validation**: Prevents double booking and booking already taken rooms
- **Cancel Booking**: Users can cancel their current booking
- **Room Switching**: Users can switch to a different room (automatically cancels old booking)
- **Full Name Display**: Shows the full name of students who have booked rooms
- **Booking Management**: Easy booking, cancellation, and viewing of room details

### 🎨 Modern UI/UX
- **Clean Design**: Modern blue color scheme with gradient effects
- **SVG Icons**: Beautiful, scalable icons throughout the interface
- **Responsive Layout**: Mobile-friendly design that works on all devices
- **Intuitive Navigation**: Easy-to-use navigation and user interface
- **Modern Footer**: Clean footer with copyright (2025) and author information

## 📋 Project Structure

```
hostel_booking/
├── hostel/                      # Main Django application
│   ├── models.py                # Database models (Block, Floor, Room, UserProfile)
│   ├── views.py                 # View functions
│   ├── forms.py                 # Custom user registration form with gender
│   ├── urls.py                  # URL routing
│   ├── admin.py                 # Admin interface configuration
│   ├── management/
│   │   └── commands/
│   │       └── populate_sample_data.py  # Management command for sample data
│   └── templates/
│       └── hostel/              # HTML templates
│           ├── base.html
│           ├── login.html
│           ├── register.html
│           ├── dashboard.html
│           ├── blocks_list.html
│           ├── block_layout.html
│           ├── room_detail.html
│           └── confirm_booking.html
├── hostel_booking/              # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/
│   └── css/
│       └── style.css            # Modern CSS styling
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Git (for cloning the repository)

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd hostel-booking
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   
   # On macOS/Linux:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Populate sample data** (optional, for testing)
   ```bash
   python manage.py populate_sample_data
   ```
   This creates:
   - 6 blocks (3 male blocks: B1, B2, B3; 3 female blocks: G1, G2, G3)
   - 18 floors (3 floors per block)
   - 90 rooms (5 rooms per floor)

6. **Create superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin account.

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - **Main Application**: http://127.0.0.1:8000/
   - **Admin Panel**: http://127.0.0.1:8000/admin/

## 📖 Usage Guide

### For Administrators

1. **Access Admin Panel**
   - Navigate to http://127.0.0.1:8000/admin/
   - Login with superuser credentials

2. **Manage Blocks**
   - Create new blocks with block name (e.g., B1, G1), gender, and description
   - Edit existing block information
   - View all blocks and their gender assignments

3. **Manage Floors**
   - Add floors to blocks (typically 3 floors per block)
   - Set floor numbers

4. **Manage Rooms**
   - Create rooms for each floor
   - Set room numbers and capacity
   - View booking status and see which student booked which room

5. **Manage User Profiles**
   - View user profiles and their gender assignments
   - Edit user information if needed

### For Students/Users

1. **Registration**
   - Navigate to `/register/`
   - Fill in:
     - Username
     - First Name
     - Last Name
     - Email (optional)
     - **Gender** (Male/Female) - **Required**
     - Password
     - Password Confirmation
   - Your gender determines which blocks you can access

2. **Login**
   - Navigate to `/login/`
   - Enter username and password

3. **View Available Blocks**
   - Click "Blocks" in the navigation
   - You will see only blocks matching your gender:
     - **Male users**: B1, B2, B3
     - **Female users**: G1, G2, G3

4. **View Block Layout**
   - Click on a block to view its layout
   - Browse available rooms organized by floors
   - Color-coded room status (green = available, red = booked)

5. **Book a Room**
   - Click on an available room
   - View room details (block, floor, capacity)
   - Click "Book This Room" button
   - **Confirmation page** will appear asking you to confirm
   - Click "Yes, Confirm Booking" to finalize

6. **Cancel Booking**
   - Go to Dashboard or Room Detail page
   - Click "Cancel Booking" button
   - Confirm in the popup dialog
   - Your booking will be cancelled

7. **Switch Rooms**
   - If you have a booking and want to change rooms
   - View another available room
   - Click "Click here to switch to this room"
   - Confirm on the confirmation page
   - Your old booking will be automatically cancelled

8. **View Dashboard**
   - Access your dashboard to see:
     - Personal information (including full name and gender)
     - Current booking details (if any)
     - Block and room information
     - Quick action links

## 🗄️ Database Models

### UserProfile
- `user`: OneToOneField to User
- `gender`: CharField - Gender of the user (M/F)

### Block
- `block_name`: CharField - Block identifier (e.g., B1, G1)
- `gender`: CharField - Gender assigned to the block (M/F)
- `description`: TextField - Description of the block

### Floor
- `block`: ForeignKey to Block
- `floor_number`: IntegerField - Floor number (typically 1-3)

### Room
- `room_number`: CharField - Room identifier
- `floor`: ForeignKey to Floor
- `capacity`: IntegerField - Maximum occupancy
- `is_booked`: BooleanField - Booking status
- `booked_by`: ForeignKey to User (nullable) - Student who booked the room

## 🎨 Design Features

- **Modern Blue Color Scheme**: Professional gradient-based design
- **SVG Icons**: Scalable vector icons for better visual appeal
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Clean UI**: Minimalist design with clear visual hierarchy
- **User-Friendly**: Intuitive navigation and clear call-to-action buttons
- **Gender Badges**: Color-coded badges for male (blue) and female (pink) blocks

## ✅ Features Implemented

- ✅ User registration with full name and gender support
- ✅ Secure login/logout functionality
- ✅ Gender-based block filtering with strict access control
- ✅ User dashboard with booking information
- ✅ Block layout visualization (grid-based)
- ✅ Room detail pages with comprehensive information
- ✅ Booking confirmation page
- ✅ Room booking system (one room per user)
- ✅ Booking cancellation functionality
- ✅ Room switching (cancel old, book new)
- ✅ Booking validation (prevents double booking)
- ✅ Full name display for booked rooms
- ✅ Modern, responsive UI with SVG icons
- ✅ Admin interface for managing blocks, floors, and rooms
- ✅ Sample data population command
- ✅ Modern footer with author credits (2025)

## 🛠️ Technology Stack

- **Backend Framework**: Django 5.2.8
- **Database**: SQLite (default, can be changed to PostgreSQL/MySQL)
- **Frontend**: HTML5, CSS3 (no JavaScript frameworks)
- **Template Engine**: Django Template Language
- **Icons**: SVG (inline)

## 📝 Important Notes

- **Gender-Based Access**: Users can only view and book rooms in blocks matching their gender
  - Male users see: B1, B2, B3
  - Female users see: G1, G2, G3
  - Access is strictly enforced - attempting to access wrong gender blocks results in error
- **One Room Per User**: Users can only book one room at a time
- **Booking Confirmation**: All bookings require confirmation before finalizing
- **Booking Cancellation**: Users can cancel their bookings at any time
- **Room Switching**: Users can switch rooms, which automatically cancels the old booking
- **Booking Status**: Booked rooms are clearly marked and cannot be booked again
- **Full Name Display**: When a room is booked, it shows "This room is already booked by another student named [Full Name]"
- **Responsive Design**: All pages are mobile-friendly and responsive
- **No JavaScript Required**: Pure HTML/CSS implementation for MVP

## 🔧 Management Commands

### Populate Sample Data
```bash
python manage.py populate_sample_data
```
Creates sample block data for testing purposes:
- 6 blocks (3 male blocks: B1, B2, B3; 3 female blocks: G1, G2, G3)
- 18 floors (3 floors per block)
- 90 rooms (5 rooms per floor)

## 📤 Uploading to GitHub

### Step 1: Initialize Git Repository

If you haven't already initialized git in your project:

```bash
cd "/Users/parthpuri/Desktop/Webtech Project"
git init
```

### Step 2: Create .gitignore File

The `.gitignore` file is already created and includes:
- Virtual environment (`venv/`)
- Database files (`db.sqlite3`)
- Python cache files (`__pycache__/`)
- IDE files (`.vscode/`, `.idea/`)
- OS files (`.DS_Store`)

### Step 3: Add Files to Git

```bash
# Add all files
git add .

# Check what will be committed
git status
```

### Step 4: Create Initial Commit

```bash
git commit -m "Initial commit: Hostel Booking System MVP

- User authentication with gender-based registration
- Block system (B1-B3 for males, G1-G3 for females)
- Room booking with confirmation and cancellation
- Gender-based access control
- Modern UI with SVG icons
- Admin interface for managing blocks, floors, and rooms"
```

### Step 5: Create GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Enter repository name (e.g., `hostel-booking-system`)
5. Choose visibility (Public or Private)
6. **DO NOT** initialize with README, .gitignore, or license (we already have these)
7. Click "Create repository"

### Step 6: Connect Local Repository to GitHub

After creating the repository, GitHub will show you commands. Use these:

```bash
# Add remote repository (replace <username> and <repo-name> with your details)
git remote add origin https://github.com/<username>/<repo-name>.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

### Step 7: Verify Upload

1. Go to your GitHub repository page
2. Verify all files are uploaded
3. Check that README.md displays correctly
4. Verify .gitignore is working (venv/ and db.sqlite3 should not be visible)

### Additional Git Commands

**To update repository after making changes:**
```bash
git add .
git commit -m "Description of changes"
git push
```

**To check repository status:**
```bash
git status
```

**To view commit history:**
```bash
git log
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Authors

**Made by Parth Puri and Nandika Mishra**

Built with ❤️ using Django

## 📞 Support

For issues, questions, or contributions, please open an issue on the GitHub repository.

---

## 🎯 Project Status

✅ **MVP Complete** - All core features implemented and tested:
- Gender-based access control working
- Booking system with confirmation and cancellation
- Room switching functionality
- Modern UI with responsive design
- Admin interface fully functional

**Note**: This is an MVP (Minimum Viable Product) version. For production use, consider adding:
- Email verification
- Payment integration
- Advanced search and filtering
- Booking history
- Email notifications
- Room transfer/cancellation requests
- Password reset functionality
- User profile editing
