from pathlib import Path
import zipfile

# Android İndirilenler klasörü
download = Path("/storage/emulated/0/Download")
download.mkdir(parents=True, exist_ok=True)

# Site klasörü
site = download / "barisma_site"
site.mkdir(parents=True, exist_ok=True)

# HTML dosyası
html = r'''<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Bir Şey Söylemek İstedim</title>

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    min-height: 100vh;
    background: #000;
    color: #fff;
    font-family: Arial, sans-serif;

    display: flex;
    justify-content: center;
    align-items: center;

    padding: 25px;
}

.whatsapp-note {
    position: fixed;
    top: 15px;
    right: 15px;

    max-width: 230px;

    color: #888;
    font-size: 12px;
    line-height: 1.4;

    text-align: right;
}

.card {
    width: 100%;
    max-width: 600px;

    text-align: center;

    padding: 35px 25px;
}

.screen {
    display: none;

    animation: fade 0.5s ease;
}

.screen.active {
    display: block;
}

h1 {
    font-size: 32px;
    margin-bottom: 25px;
}

p {
    color: #ddd;

    font-size: 18px;
    line-height: 1.8;
}

button {
    border: none;
    border-radius: 30px;

    padding: 14px 28px;
    margin: 15px 5px;

    font-size: 16px;

    cursor: pointer;

    transition: 0.2s;
}

button:hover {
    transform: translateY(-2px);
}

.primary {
    background: white;
    color: black;
}

.secondary {
    background: transparent;
    color: white;

    border: 1px solid #555;
}

@keyframes fade {

    from {
        opacity: 0;
        transform: translateY(15px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }

}

@media (max-width: 500px) {

    h1 {
        font-size: 27px;
    }

    p {
        font-size: 16px;
    }

}
</style>
</head>

<body>

<div class="whatsapp-note">
Seçimini yaptıktan sonra WhatsApp'tan yazabilirsin. 🤍
</div>

<div class="card">

    <!-- 1. NOT -->

    <section class="screen active" id="screen1">

        <h1>Öncelikle...</h1>

        <p>
            Öncelikle nasılsın diye sormak istedim.
            Umarım iyisindir.
        </p>

        <button class="primary" onclick="showScreen(2)">
            Devam
        </button>

    </section>


    <!-- 2. NOT -->

    <section class="screen" id="screen2">

        <h1>Sana söylemek istediğim bir şey var.</h1>

        <p>
            Bunu sadece barışalım diye değil,
            sana gerçekten ne kadar değer verdiğimi göstermek için yaptım.
            Aramızda ne yaşandıysa yaşandı, ama seni kırdığım yerleri düşündüm.
            Her şeyi bir anda düzeltemeyeceğimi biliyorum.
            Sadece bir şans daha verip, bu sefer laflarla değil
            davranışlarımla göstermek istiyorum.
            Seni kaybetmek istemiyorum.
        </p>

        <button class="primary" onclick="choose(true)">
            Barışalım
        </button>

        <button class="secondary" onclick="choose(false)">
            Barışmayalım
        </button>

    </section>


    <!-- SONUÇ -->

    <section class="screen" id="screen3">

        <h1 id="resultTitle"></h1>

        <p id="resultText"></p>

        <button class="primary" onclick="location.reload()">
            Başa Dön
        </button>

    </section>

</div>


<script>

function showScreen(number) {

    document.querySelectorAll(".screen").forEach(function(screen) {

        screen.classList.remove("active");

    });

    document
        .getElementById("screen" + number)
        .classList.add("active");
}


function choose(yes) {

    if (yes) {

        document.getElementById("resultTitle").innerText =
            "Teşekkür ederim. 🤍";

        document.getElementById("resultText").innerText =
            "Her şeyi bir anda düzeltmek zorunda değiliz. " +
            "Bu sefer sözlerle değil, davranışlarımla göstermeye çalışacağım.";

    }

    else {

        document.getElementById("resultTitle").innerText =
            "Kararına saygı duyuyorum.";

        document.getElementById("resultText").innerText =
            "Bunu sadece barışalım diye değil, " +
            "sana gerçekten ne hissettiğimi söyleyebilmek için yaptım. " +
            "Her şeye rağmen okuduğun için teşekkür ederim. 🤍";

    }

    showScreen(3);
}

</script>

</body>
</html>
'''

# index.html oluştur
html_file = site / "index.html"

html_file.write_text(
    html,
    encoding="utf-8"
)


# ZIP oluştur
zip_file = download / "barisma_site.zip"

with zipfile.ZipFile(
    zip_file,
    "w",
    zipfile.ZIP_DEFLATED
) as z:

    z.write(
        html_file,
        "index.html"
    )


print()
print("================================")
print("       SITE HAZIR!")
print("================================")
print()
print("INDEX:")
print(html_file)
print()
print("ZIP:")
print(zip_file)
print()
print("GitHub'a yüklemek için:")
print("Download > barisma_site.zip")
print()
print("Bitti.")