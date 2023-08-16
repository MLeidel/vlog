<?php
/***
    use: include "../libsvlog.php"; in the index.php file.
    Creates a vlog.txt entry for each external visitor
    to a website.
***/

$raddr = $_SERVER[REMOTE_ADDR];
$usrag = str_replace(",", "·", $_SERVER[HTTP_USER_AGENT]);  // often has commas
//$raddr = "111.111.11.1";  // for testing an external IP
$check = substr($raddr, 0, 7);
if ($check != "192.168") {  // only log external requests
  $data = $raddr . "," . date("Y-m-d H:i:s") . "," . $usrag . "\n";
  file_put_contents( "vlog.txt", $data, FILE_APPEND );
}
?>
