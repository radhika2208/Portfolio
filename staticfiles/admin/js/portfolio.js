  var textArray = [
    "Backend Developer",
    "Web Designer",
    "Problem Solver",
    "Blog Writer"
  ];

  var typingText = document.getElementById("typing-text");
  var index = 0;
  var currentText = "";
  var letter = "";
  var typingIcon = '<span class="typing-icon">|</span>'; // Typing icon HTML

  function type() {
    if (index === textArray.length) {
      index = 0;
    }

    currentText = " " + textArray[index];
    letter = currentText.slice(0, ++letterCount);

    typingText.innerHTML = letter + typingIcon; // Append typing icon HTML

    if (letter.length === currentText.length) {
      setTimeout(function() {
        erase();
      }, 2000);
    } else {
      setTimeout(type, 100);
    }
  }

  function erase() {
    letter = currentText.slice(0, --letterCount);

    typingText.innerHTML = letter + typingIcon; // Append typing icon HTML

    if (letter.length === 0) {
      index++;
      if (index === textArray.length) {
        index = 0;
      }
      currentText = "I am a " + textArray[index];
      setTimeout(type, 200);
    } else {
      setTimeout(erase, 50);
    }
  }

  var letterCount = 0;
  setTimeout(type, 2000);
