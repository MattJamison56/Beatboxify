var extensionIsDisabled
var appearChance
var flipChance

// Function to load settings from Chrome storage
function loadSettings() {
    chrome.storage.local.get({
        extensionIsDisabled: false,
        appearChance: 1.00,
        flipChance: 0.25
    }, function (data) {
        document.getElementById('disableExtension').checked = !data.extensionIsDisabled;
    });
}

// Function to save settings to Chrome storage
function saveSettings() {
    const data = {
        extensionIsDisabled: !document.getElementById('disableExtension').checked,
    };

    chrome.storage.local.set(data, () => {
        if (chrome.runtime.lastError) {
            console.error("Error saving settings:", chrome.runtime.lastError);
        } else {
            console.log("Settings saved successfully.");
        }
    });
}

function ChangeNameInHeading() {
    // Get the extension name
    let extensionName = chrome.runtime.getManifest().name;

    // Remove "youtube" (case-insensitive) from the extension name and trim
    extensionName = extensionName.replace(/youtube/i, '').trim();

    // Replace "Beatboxify" in the title with the cleaned extension name
    const titleElement = document.getElementById('extension-title');
    titleElement.textContent = titleElement.textContent.replace('TITLE', extensionName);
}

// Call loadSettings() when the page loads
document.addEventListener('DOMContentLoaded', loadSettings);

// Add input event listeners to all input fields to trigger autosave
document.getElementById('disableExtension').addEventListener('input', saveSettings);

document.addEventListener('DOMContentLoaded', ChangeNameInHeading);
