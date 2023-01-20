package Caeser_Cipher;

public class CaeserCipher{
    public static void main(String[] args) {
        String msg = "zzz";
        msg = msg.toUpperCase();
        int key = 1;
        int shift = key%26;
        String encrypted = "";

        for(int i=0;i<msg.length();i++){
            encrypted+=(char)(((int)msg.charAt(i)+shift - 65)%26 + 65);
        }

        System.out.println(encrypted);
    }
}
