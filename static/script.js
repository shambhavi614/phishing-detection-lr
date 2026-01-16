function checkURL() {
  const url = document.getElementById("url").value;
  const resultBox = document.getElementById("result");

  if (!url) {
    resultBox.style.display = "block";
    resultBox.className = "result phishing";
    resultBox.innerText = "⚠️ Please enter a valid URL";
    return;
  }

  resultBox.style.display = "block";
  resultBox.className = "result";
  resultBox.innerText = "🔍 Scanning website...";

  fetch("/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ url: url })
  })
  .then(res => res.json())
  .then(data => {
    if (data.result.includes("Phishing")) {
      resultBox.classList.add("phishing");
      resultBox.innerText = "🚨 Phishing Website Detected!";
    } else {
      resultBox.classList.add("safe");
      resultBox.innerText = "✅ This Website is Safe";
    }
  })
  .catch(() => {
    resultBox.classList.add("phishing");
    resultBox.innerText = "❌ Server Error. Try again.";
  });
}
