document.addEventListener('DOMContentLoaded', () => {
    const analyzeBtn = document.getElementById('analyzeBtn');
    const emailInput = document.getElementById('emailInput');
    const resultSection = document.getElementById('results');
    const resultsContent = document.getElementById('resultsContent');
    const stats = document.querySelectorAll('.stats-box .circle span');
    
  stats.forEach((stat) => {
    const target = parseInt(stat.textContent);
    stat.textContent = '0';

    const increment = Math.ceil(target / 100); // Adjust speed
    let count = 0;

    const updateCount = () => {
      count += increment;
      if (count > target) {
        count = target;
      }
      stat.textContent = count + '%';
      if (count < target) {
        requestAnimationFrame(updateCount);
      }
    };

    updateCount();
  });
});
    analyzeBtn.addEventListener('click', () => {
        const email = emailInput.value.trim();
        if (!email) {
            alert('Please enter your email to analyze!');
            return;
        }

        // Simulate API Response
        const mockData = {
            totalEmails: 100,
            phishingEmails: 7,
            details: [
                { subject: "Win a $1000 Gift Card!", type: "Phishing", confidence: "92%" },
                { subject: "Account Verification Required", type: "Phishing", confidence: "85%" },
            ],
        };

        resultsContent.innerHTML = `
            <p><strong>Total Emails Analyzed:</strong> ${mockData.totalEmails}</p>
            <p><strong>Phishing Emails Found:</strong> ${mockData.phishingEmails}</p>
            <h3>Email Details:</h3>
            <ul>
                ${mockData.details
                    .map(
                        (email) =>
                            `<li><strong>${email.subject}</strong> - ${email.type} (${email.confidence} confidence)</li>`
                    )
                    .join('')}
            </ul>
        `;
        resultSection.classList.remove('hidden');
    });
    
    document.getElementById("contactForm").addEventListener("submit", function (e) {
        e.preventDefault(); // Prevent the default form submission
      
        // Initialize EmailJS with your user ID
        emailjs.init("YOUR_EMAILJS_USER_ID"); // Replace with your EmailJS user ID
      
        // Collect form data
        const formData = {
          name: document.getElementById("name").value,
          email: document.getElementById("email").value,
          message: document.getElementById("message").value,
        };
      
        // Send the email
        emailjs.send("YOUR_SERVICE_ID", "YOUR_TEMPLATE_ID", formData)
          .then(() => {
            alert("Your message has been sent successfully!");
            document.getElementById("contactForm").reset(); // Reset the form
          })
          .catch((error) => {
            console.error("EmailJS Error:", error);
            alert("There was an error sending your message. Please try again.");
          });
      });
      document.getElementById("analyzeForm").addEventListener("submit", function (e) {
        e.preventDefault(); // Prevent default form submission
      
        // Get input values
        const email = document.getElementById("emailInput").value.trim();
        const password = document.getElementById("passwordInput").value.trim();
      
        // Validate inputs
        if (!email || !validateEmail(email)) {
          alert("❌ Please enter a valid email address.");
          return;
        }
      
        if (!password || password.length < 8) {
          alert("❌ Password must be at least 8 characters long.");
          return;
        }
      
        // If validation passes
        alert("✅ Inputs are valid. Analyzing your inbox...");
        // Add functionality to handle analysis here
      });
      
      // Email validation function
      function validateEmail(email) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(email);
      }
      document.getElementById("analyzeForm").addEventListener("submit", function (e) {
        e.preventDefault(); // Prevent the default form submission behavior
      
        // Disable the Analyze button to prevent multiple clicks
        const analyzeBtn = document.getElementById("analyzeBtn");
        analyzeBtn.disabled = true;
        analyzeBtn.textContent = "Processing...";
      
        // Define the progress messages and their respective delays
        const messages = [
          { text: "🔐 Generating credentials file...", delay: 5000 }, // 5 seconds
          { text: "✅ Credentials.yml generated successfully.", delay: 5000 }, // 5 seconds
          { text: "📤 Extracting data from email...", delay: 20000 }, // 20 seconds
          { text: "📊 Report generated successfully.", delay: 10000 } // 10 seconds
        ];
      
        let currentMessage = 0;
      
        // Function to display messages in sequence
        const statusContainer = document.createElement("div");
        statusContainer.id = "statusContainer";
        statusContainer.style.textAlign = "center";
        statusContainer.style.marginTop = "20px";
        document.getElementById("analyze").appendChild(statusContainer);
      
        const showMessage = () => {
          if (currentMessage < messages.length) {
            const messageElement = document.createElement("p");
            messageElement.textContent = messages[currentMessage].text;
            messageElement.style.margin = "10px 0";
            messageElement.style.color = "#00FF7F"; // Highlight in green
            statusContainer.appendChild(messageElement);
      
            // Wait for the delay specified for the current step, then proceed
            setTimeout(() => {
              currentMessage++;
              showMessage();
            }, messages[currentMessage].delay);
          } else {
            // Enable button and redirect to view the report
            const reportLink = document.createElement("a");
            reportLink.href = "report.html"; // Replace with the actual report URL
            reportLink.textContent = "➡️ View Report";
            reportLink.style.display = "inline-block";
            reportLink.style.marginTop = "20px";
            reportLink.style.padding = "10px 20px";
            reportLink.style.background = "#00BFA5";
            reportLink.style.color = "white";
            reportLink.style.borderRadius = "5px";
            reportLink.style.textDecoration = "none";
            reportLink.style.transition = "all 0.3s ease";
      
            reportLink.onmouseover = function () {
              this.style.background = "#00897B";
              this.style.transform = "scale(1.05)";
            };
      
            reportLink.onmouseout = function () {
              this.style.background = "#00BFA5";
              this.style.transform = "scale(1)";
            };
      
            statusContainer.appendChild(reportLink);
            analyzeBtn.disabled = false;
            analyzeBtn.textContent = "Analyze";
          }
        };
      
        // Start showing messages
        showMessage();
      });
      