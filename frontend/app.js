// Get the form and table elements
const form = document.getElementById('studentForm');
const studentTable = document.getElementById('studentTable').getElementsByTagName('tbody')[0];
let students = []; // Array to store student data temporarily

// Add event listener to the form
form.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from refreshing the page

    const studentId = document.getElementById('studentId').value;
    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;
    const dob = document.getElementById('dob').value;
    const gender = document.getElementById('gender').value;
    const phone = document.getElementById('phone').value;
    const email = document.getElementById('email').value;
    const course = document.getElementById('course').value;

    // Add new student or update existing student
    if (studentId) {
        updateStudent(studentId, firstName, lastName, dob, gender, phone, email, course);
    } else {
        addStudent(firstName, lastName, dob, gender, phone, email, course);
    }

    form.reset(); // Clear the form
});

// Function to add a new student
function addStudent(firstName, lastName, dob, gender, phone, email, course) {
    const newStudent = {
        id: students.length + 1,
        firstName,
        lastName,
        dob,
        gender,
        phone,
        email,
        course
    };
    students.push(newStudent);
    renderTable();
}

// Function to view all students
function viewStudents() {
    renderTable();
}

// Function to render the table with student data
function renderTable() {
    // Clear existing rows
    studentTable.innerHTML = '';

    students.forEach(student => {
        const newRow = studentTable.insertRow();
        newRow.innerHTML = `
            <td>${student.id}</td>
            <td>${student.firstName} ${student.lastName}</td>
            <td>${student.dob}</td>
            <td>${student.gender}</td>
            <td>${student.phone}</td>
            <td>${student.email}</td>
            <td>${student.course}</td>
            <td>
                <button onclick="editStudent(${student.id})">Edit</button>
                <button onclick="deleteStudent(${student.id})">Delete</button>
            </td>
        `;
    });
}

// Function to edit student information
function editStudent(id) {
    const student = students.find(student => student.id === id);
    document.getElementById('studentId').value = student.id;
    document.getElementById('firstName').value = student.firstName;
    document.getElementById('lastName').value = student.lastName;
    document.getElementById('dob').value = student.dob;
    document.getElementById('gender').value = student.gender;
    document.getElementById('phone').value = student.phone;
    document.getElementById('email').value = student.email;
    document.getElementById('course').value = student.course;
}

// Function to delete a student
function deleteStudent(id) {
    const index = students.findIndex(student => student.id === id);
    if (index > -1) {
        students.splice(index, 1); // Remove student from array
        renderTable();
    }
}
