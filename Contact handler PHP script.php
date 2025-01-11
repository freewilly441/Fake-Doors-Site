<?php
// contact_handler.php

// Check if form was submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize inputs
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $message = htmlspecialchars($_POST['message']);
    
    // Save the data to a file (or use a database)
    $file = fopen("contact_logs.txt", "a");
    fwrite($file, "Name: $name\nEmail: $email\nMessage: $message\n\n");
    fclose($file);

    // Redirect back to the homepage or thank you page
    header("Location: thank_you.html");
    exit();
} else {
    // Redirect to the homepage if accessed directly
    header("Location: index.html");
    exit();
}
?>
