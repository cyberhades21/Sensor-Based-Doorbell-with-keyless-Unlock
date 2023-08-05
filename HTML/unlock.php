
<?php
    system("sudo python lock.py");
    echo"unlocked";
    header("Location:index.php");
    exit();
?>
