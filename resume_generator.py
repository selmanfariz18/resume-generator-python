import pdfkit

def get_user_input(prompt):
    return input(prompt).strip()

def generate_resume_content(name, email, mobile, gender, qualification, college, specialization, grad_year):
    return f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; }}
            .container {{ margin: 0 auto; padding: 20px; width: 60%; }}
            .header {{ text-align: center; margin-bottom: 40px; }}
            .section {{ margin-bottom: 20px; }}
            .section p {{ margin: 5px 0; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Resume</h1>
            </div>
            <div class="section">
                <p><strong>Name:</strong> {name}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Mobile Number:</strong> {mobile}</p>
                <p><strong>Gender:</strong> {gender}</p>
                <p><strong>Highest Qualification:</strong> {qualification}</p>
                <p><strong>College:</strong> {college}</p>
                <p><strong>Specialization/Branch:</strong> {specialization}</p>
                <p><strong>Year of Graduation:</strong> {grad_year}</p>
            </div>
        </div>
    </body>
    </html>
    """

def main():
    print("Enter the following details to generate your resume:")

    name = get_user_input("Name: ")
    email = get_user_input("Email: ")
    mobile = get_user_input("Mobile Number: ")
    gender = get_user_input("Gender: ")
    qualification = get_user_input("Highest Qualification: ")
    college = get_user_input("College: ")
    specialization = get_user_input("Specialization/Branch: ")
    grad_year = get_user_input("Year of Graduation: ")

    resume_content = generate_resume_content(name, email, mobile, gender, qualification, college, specialization, grad_year)

    # Save the resume content to an HTML file
    with open("resume.html", "w") as file:
        file.write(resume_content)

    # Convert HTML to PDF
    pdfkit.from_file("resume.html", "resume.pdf")

    print("Resume has been generated and saved as resume.pdf")

if __name__ == "__main__":
    main()

