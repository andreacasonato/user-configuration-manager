# A User Configuration Manager that allows users to manage their settings such as theme, language, and notifications.
# Will implement functions to add, update, delete, and view user settings.

# Test data
test_settings = {
    "theme": "dark",
    "language": "english",
    "notifications": "enabled"
}

# Add a new setting
def add_setting(settings, key_value_tuple):
    key = key_value_tuple[0].lower()
    value = key_value_tuple[1].lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

# Update an existing setting
def update_setting(settings, key_value_tuple):
    key = key_value_tuple[0].lower()
    value = key_value_tuple[1].lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"

    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

# Delete a setting
def delete_setting(settings, key):
    key = key.lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"

    return "Setting not found!"

# View all settings
def view_settings(settings):
    if not settings:
        return "No settings available."

    result = "Current User Settings:\n"
    for key, value in settings.items():
        result += f"{key.capitalize()}: {value}\n"

    return result