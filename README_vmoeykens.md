# XSS Attack Vulnerability Fix
Vincent Moeykens
### How the attack worked.
In the original `CatCoin_Stock.html` file, there was a line in the head tag that looked like this:
```
<script src="https://jreddy1.w3.uvm.edu/getStock.js"></script>
```
Because the integrity of this resource was not being checked, it was possible to for a XSS attack to be executed 
and replace the returned file with a malicious one. 
### How the vulnerability was fixed.
In order to fix this, I generated an SRI hash using the SHA-384 algorithm and created a new script tag that 
included the hash. This was generated using this website: [here]("https://www.srihash.org/"). The new tag looks like
this:
```
    <script src="https://jreddy1.w3.uvm.edu/getStock.js"
            integrity="sha384-eLjZLjnEqrqfoIzgU/ObMimoH+M3VIrXBaNuJyCDBRARMwzvENHbNIOs8PgnaJUT" crossorigin="anonymous">
```
Now when the file is loaded from the CDN, the integrity is checked by the browser by comparing the generated hashes,
and if it doesn't match it doesn't load the file and we get an error such as: 
```
Failed to find a valid digest in the 'integrity' attribute for resource 'https://jreddy1.w3.uvm.edu/getStock.js' with computed SHA-256 integrity 'CKRbov6rxN3K/FQyaC/WGnToue7lv89/Pd3k3I12Ls0='. The resource has been blocked.
```
I also verified that all other remote resources are being checked by their SRI hash. 