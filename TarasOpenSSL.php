<?php
$cipherMode = "AES-128-CTR"; //обираємо режим шифрування/дешифрування
$cipherText = file_get_contents('cipherText.txt'); //читаємо вміст файлу з шифротекстом
$plaintext = "something plaintext";
$key = $argv[1]; //зчитуємо ключ як перший аргумент командного рядку
$iv = $argv[2]; //зчитуємо вектор ініціалізації як другий аргумент командного рядку
$exeMode = $argv[3]; //зчитуємо режим роботи програми як третій аргумент командного рядку
if (in_array($cipherMode, openssl_get_cipher_methods()))
{
	if ($exeMode == 'dec') //якщо режим роботи "dec", виконуємо дешифрацію заданого шифротексту
	{
    	$sourceText = openssl_decrypt($cipherText, $cipherMode, $key, $options=0, $iv);
    	echo $sourceText."\n";
    }
    else
    {
        $ciphertext = openssl_encrypt($plaintext, $cipherMode, $key, $options=0, $iv);
        echo $ciphertext."\n";
    }
}
?>