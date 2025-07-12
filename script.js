
document.getElementById("nextBtn").onclick = () => {
  const aadhaar = document.getElementById("aadhaar").value;
  const aadhaarError = document.getElementById("aadhaarError");
  if (!/^\d{12}$/.test(aadhaar)) {
    aadhaarError.textContent = "Aadhaar must be 12 digits.";
  } else {
    aadhaarError.textContent = "";
    document.querySelector(".step-1").classList.add("hidden");
    document.querySelector(".step-2").classList.remove("hidden");
  }
};

document.getElementById("backBtn").onclick = () => {
  document.querySelector(".step-2").classList.add("hidden");
  document.querySelector(".step-1").classList.remove("hidden");
};

document.getElementById("pincode").addEventListener("keyup", async (e) => {
  const pin = e.target.value;
  if (/^\d{6}$/.test(pin)) {
    try {
      const res = await fetch("https://api.postalpincode.in/pincode/" + pin);
      const data = await res.json();
      if (data[0].Status === "Success") {
        document.getElementById("state").value = data[0].PostOffice[0].State;
        document.getElementById("city").value = data[0].PostOffice[0].District;
      } else {
        document.getElementById("state").value = "";
        document.getElementById("city").value = "";
      }
    } catch (err) {
      console.error("PIN API Error:", err);
    }
  }
});

document.getElementById("udyamForm").onsubmit = (e) => {
  e.preventDefault();
  const pan = document.getElementById("pan").value;
  const panError = document.getElementById("panError");
  if (!/^[A-Z]{5}[0-9]{4}[A-Z]{1}$/.test(pan)) {
    panError.textContent = "Invalid PAN format.";
  } else {
    panError.textContent = "";
    alert("Form submitted (fake)!");
  }
};
