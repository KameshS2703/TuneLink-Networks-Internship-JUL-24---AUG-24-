require.config({ paths: { 'vs': 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.31.1/min/vs' }});
require(['vs/editor/editor.main'], function() {
    const editorElement = document.getElementById('editor');
    const languageSelect = document.getElementById('language-select');
    const outputElement = document.getElementById('output');

    window.editor = monaco.editor.create(editorElement, {
        value: '',
        language: 'python',
        theme: 'vs-dark'
    });

    languageSelect.addEventListener('change', function() {
        const selectedLanguage = languageSelect.value;
        let defaultValue = '';

        switch (selectedLanguage) {
            case 'c':
                defaultValue = `#include <stdio.h>\n\nint main() {\n    printf("Hello, C World!\\n");\n    return 0;\n}`;
                break;
            case 'cpp':
                defaultValue = `#include <iostream>\n\nint main() {\n    std::cout << "Hello, C++ World!" << std::endl;\n    return 0;\n}`;
                break;
            case 'java':
                defaultValue = `public class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println("Hello, Java World!");\n    }\n}`;
                break;
            case 'python':
                defaultValue = `print("Hello, Python World!")`;
                break;
            case 'sql':
                defaultValue = `SELECT * FROM table_name;`;
                break;
        }

        window.editor.setValue(defaultValue);
        monaco.editor.setModelLanguage(window.editor.getModel(), selectedLanguage);
    });

    window.editor.setValue(`print("Hello, Python World!")`);
});

function saveCode() {
    const language = document.getElementById('language-select').value;
    const code = window.editor.getValue();
    fetch('/save', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ language: language, code: code })
    })
    .then(response => response.json())
    .then(data => alert(data.message))
    .catch(error => console.error('Error:', error));
}

function runCode() {
    const language = document.getElementById('language-select').value;
    const code = window.editor.getValue();
    fetch('/run', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ language: language, code: code })
    })
    .then(response => response.json())
    .then(data => {
        const outputElement = document.getElementById('output');
        outputElement.textContent = data.output;
    })
    .catch(error => console.error('Error:', error));
}
