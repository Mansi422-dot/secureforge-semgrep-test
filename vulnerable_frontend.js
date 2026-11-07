// INTENTIONALLY VULNERABLE training examples. Never deploy this file.
function renderUserInput(element, userInput) {
  element.innerHTML = userInput;
  document.write(userInput);
}

function runDynamicCode(source) {
  return eval(source);
}
