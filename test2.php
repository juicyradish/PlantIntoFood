<?php
    echo("hello");

    if(isset($_POST['submit'])) {
        $file = $_FILES['file'];
    
        print_r($file);
        $fileName = $_FILES['file']['name'];
    }