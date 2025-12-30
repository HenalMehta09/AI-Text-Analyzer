const BACKEND_URL = window.BACKEND_URL || "http://localhost:8000";

async function analyze() {
  const text = document.getElementById("textInput").value;

  if (!text) {
    alert("Please enter some text");
    return;
  }

  const response = await fetch(
    `${BACKEND_URL}/predict?text=${encodeURIComponent(text)}`
  );

  const data = await response.json();
  document.getElementById("result").textContent =
    JSON.stringify(data, null, 2);
}
