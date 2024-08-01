function submitAppointment() {
    // Implement logic to handle the appointment submission
    const appointmentDetails = {
        name: document.getElementById("name").value,
        age: document.getElementById("age").value,
        gender: document.getElementById("gender").value,
        appointmentType: document.getElementById("appointmentType").value,
        healthConcern: document.getElementById("healthConcern").value,
        doctor: document.getElementById("doctor").value,
        time: document.getElementById("time").value,
        phone: document.getElementById("phone").value,
        emailNotification: document.getElementById("emailNotification").checked,
        smsNotification: document.getElementById("smsNotification").checked,
        pushNotification: document.getElementById("pushNotification").checked,
    };

    // Add your logic to process the appointment details (e.g., send to a server)
    console.log(appointmentDetails);

    // Display a confirmation message (you can customize this)
    const confirmationUrl = `confirmationPage.html?name=${appointmentDetails.name}&time=${appointmentDetails.time}&doctor=${appointmentDetails.doctor}`;
    
    window.location.href = confirmationUrl;
}
