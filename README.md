# discord-sound-board

This bot is designed to have a less limited sound board version in discord.

## setup

### Creating a bot

1. Go to the discord developer portal: https://discord.com/developers/applications
2. Make a new application by clicking the button in the top right.
3. Go to the bot menu and scroll down to the bot permissions
4. Give the bot admin rights as the permissions. If you want to be more specific look [Here](#permissions)
5. You can fiddle around with permissions if you like, but giving the bot admin rights is the easiest.
6. Scroll up again and click on reset token
7. Copy the token
8. Rename the .env_example to .env and place the token in there
9. Go to the OAuth2 menu and then URL Generator
10. For the scope select bot and for permissions the same as 4.
11. Copy the generated URL and open it in a new browser window
12. Select the server and add the bot

### Configuring the bot

1. Open discord
2. Go to the settings -> Advanced and enable developer mode
3. Right click the server with the bot
4. Click on Copy Server ID (if this doesnt show you do not have developer mode enabled)
5. Paste the server id in the .env file

### Adding ffmpeg

1. Download the latest release for your platform from here: https://github.com/BtbN/FFmpeg-Builds/releases (or [this](https://github.com/BtbN/FFmpeg-Builds/releases/tag/autobuild-2023-09-22-12-51) one if it fails)
2. Extract it into this project in a folder called ffmpeg. The structure should look like this:
   ```
   cogs/
   ffmpeg/
   ├─ bin/
   ├─ lib/
   ├─ LICENSE.txt
   main.py
   ...
   ```

### Starting the bot

1. Install the requirements from the requirements.txt (how you wanna do this is up to you (venv/root/docker))
2. run main.py
3. The bot should now come online on discord and using its slash commandos you can add/remove sounds and open the board.

#### Permissions

These are likely the permissions you should give to the bot

- send messages,
- use slash commands
- use embedded activities
- connect
- speak
