<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<title>Ignoble Epub DeDRM Plugin Configuration</title>
</head>

<body>

<h1>Ignoble Epub DeDRM Plugin</h1>
<h3>(version 0.2.6)</h3>
<h3> For additional help read the <a href="http://apprenticealf.wordpress.com/2011/01/17/frequently-asked-questions-about-the-drm-removal-tools/" target="_blank">FAQ</a> on <a href="http://apprenticealf.wordpress.com" target="_blank">Apprentice Alf's Blog</a> and ask questions in the comments section of the <a href="http://apprenticealf.wordpress.com/2012/09/10/drm-removal-tools-for-ebooks/" target="_blank">first post</a>.</h3>

<p>All credit given to I ♥ Cabbages for the original standalone scripts (I had the much easier job of converting them to a calibre plugin).</p>

<p>This plugin is meant to decrypt Barnes & Noble ePubs that are protected with Adobe's Adept encryption. It is meant to function without having to install any dependencies... other than having calibre installed, of course. It will still work if you have Python and PyCrypto already installed, but they aren't necessary.</p>

<p>This help file is always available from within the plugin's customization dialog in calibre (when installed, of course). The "Plugin Help" link can be found in the upper-right portion of the customization dialog.</p> 

<h3>Installation:</h3>

<p>Go to calibre's Preferences page.  Do **NOT** select "Get plugins to enhance calibre" as this is reserved for "official" calibre plugins, instead select "Change calibre behavior". Under "Advanced" click on the Plugins button. Use the "Load plugin from file" button to select the plugin's zip file  (ignobleepub_v02.3_plugin.zip) and click the 'Add' button. Click 'Yes' in the the "Are you sure?" dialog. Click OK in the "Success" dialog. <b><u>Now restart calibre</u></b>.</p>


<h3>Configuration:</h3>

<p>Upon first installing the plugin (or upgrading from a version earlier than 0.2.0), the plugin will be unconfigured. Until you create at least one B&amp;N key&mdash;or migrate your existing key(s)/data from an earlier version of the plugin&mdash;the plugin will not function. When unconfigured (no saved keys)... an error message will occur whenever ePubs are imported to calibre. To eliminate the error message, open the plugin's customization dialog and create/import/migrate a key (or disable/uninstall the plugin). You can get to the plugin's customization dialog by opening calibre's Preferences dialog, and clicking Plugins (under the Advanced section). Once in the Plugin Preferences, expand the "File type plugins" section and look for the "Ignoble Epub DeDRM" plugin. Highlight that plugin and click the "Customize plugin" button.</p>

<p>If you are upgrading from an earlier version of this plugin and have provided your name(s) and credit card number(s) as part of the old plugin's customization string, you will be prompted to migrate this data to the plugin's new, more secure, key storage method when you open the customization dialog for the first time. If you choose NOT to migrate that data, you will be prompted to save that data as a text file in a location of your choosing. Either way, this plugin will no longer be storing names and credit card numbers in plain sight (or anywhere for that matter) on your computer or in calibre. If you don't choose to migrate OR save the data, that data will be lost. You have been warned!!</p>

<p>Upon configuring for the first time, you may also be asked if you wish to import your existing *.b64 keyfiles (if you use them) to the plugin's new key storage method. The new plugin no longer looks for keyfiles in calibre's configuration directory, so it's highly recommended that you import any existing keyfiles when prompted ... but you <i>always</i> have the ability to import existing keyfiles anytime you might need/want to.</p>

<p>If you have upgraded from an earlier version of the plugin, the above instructions may be all you need to do to get the new plugin up and running. Continue reading for new-key generation and existing-key management instructions.</p>

<h4 style="margin-left: 1.0em;"><u>Creating New Keys:</u></h4>

<p style="margin-left: 1.0em">On the right-hand side of the plugin's customization dialog, you will see a button with an icon that looks like a green plus sign (+). Clicking this button will open a new dialog for entering the necessary data to generate a new key.</p>
<ul style="margin-left: 2.0em;">
<li><b>Unique Key Name:</b> this is a unique name you choose to help you identify the key after it's created. This name will show in the list of configured keys. Choose something that will help you remember the data (name, cc#) it was created with.</i>
<li style="margin-top: 0.5em;"><b>Your Name:</b> Your name as set in your Barnes & Noble account, My Account page, directly under PERSONAL INFORMATION. It is usually just your first name and last name separated by a space. This name will not be stored anywhere on your computer or in calibre. It will only be used in the creation of the one-way hash/key that's stored in the preferences.</i>
<li style="margin-top: 0.5em;"><b>Credit Card#:</b> this is the default credit card number that was on file with Barnes & Noble at the time of download of the ebook to be de-DRMed. Nothing fancy here; no dashes or spaces ... just the 16 (15 for American Express) digits. Again... this number will not be stored anywhere on your computer or in calibre. It will only be used in the creation of the one-way hash/key that's stored in the preferences.</i> 
</ul> 

<p style="margin-left: 1.0em;">Click the 'OK" button to create and store the generated key. Or Cancel if you didn't want to create a key.</p>

<h4 style="margin-left: 1.0em;"><u>Deleting Keys:</u></h4>

<p style="margin-left: 1.0em;">On the right-hand side of the plugin's customization dialog, you will see a button with an icon that looks like a red "X". Clicking this button will delete the highlighted key in the list. You will be prompted once to be sure that's what you truly mean to do. Once gone, it's permanently gone.</p>

<h4 style="margin-left: 1.0em;"><u>Exporting Keys:</u></h4>

<p style="margin-left: 1.0em;">On the right-hand side of the plugin's customization dialog, you will see a button with an icon that looks like a computer's hard-drive. Use this button to export the highlighted key to a file (*.b64). Used for backup purposes or to migrate key data to other computers/calibre installations. The dialog will prompt you for a place to save the file.</p>

<h4 style="margin-left: 1.0em;"><u>Importing Existing Keyfiles:</u></h4>

<p style="margin-left: 1.0em;">At the bottom-left of the plugin's customization dialog, you will see a button labeled "Import Existing Keyfiles". Use this button to import existing *.b64 keyfiles. Used for migrating keyfiles from older versions of the plugin (or keys generated with the original I &lt;3 Cabbages script), or moving keyfiles from computer to computer, or restoring a backup. Some very basic validation is done to try to avoid overwriting already configured keys with incoming, imported keyfiles with the same base file name, but I'm sure that could be broken if someone tried hard. Just take care when importing.</p>

<p>Once done creating/importing/exporting/deleting decryption keys; click "OK" to exit the customization dialogue (the cancel button will actually work the same way here ... at this point all data/changes are committed already, so take your pick).</p>

<h3>Troubleshooting:</h3>

<p style="margin-top: 0.5em;">If you find that it's not working for you (imported Barnes & Noble epubs still have DRM), you can save a lot of time and trouble by trying to add the epub to Calibre with the command line tools. This will print out a lot of helpful debugging info that can be copied into any online help requests. I'm going to ask you to do it first, anyway, so you might as well get used to it. ;)</p>

<p>Open a command prompt (terminal) and change to the directory where the ebook you're trying to import resides. Then type the command "calibredb add your_ebook.epub" **. Don't type the quotes and obviously change the 'your_ebook.epub' to whatever the filename of your book is. Copy the resulting output and paste it into any online help request you make.</p>

<p>Another way to debug (perhaps easier if you're not all that comfortable with command-line stuff) is to launch calibre in debug mode. Open a command prompt (terminal) and type "calibre-debug -g" (again without the quotes). Calibre will launch, and you can can add the problem book(s) using the normal gui method. The debug info will be output to the original command prompt (terminal window). Copy the resulting output and paste it into any online help request you make.</p>
<p>&nbsp;</p>
<p>** Note: the Mac version of Calibre doesn't install the command line tools by default. If you go to the 'Preferences' page and click on the miscellaneous button, you'll see the option to install the command line tools.</p>

<p>&nbsp;</p>
<h4>Revision history:</h4>
<pre>
   0.1.0 - Initial release
   0.1.1 - Allow Windows users to make use of openssl if they have it installed.
          - Incorporated SomeUpdates zipfix routine.
   0.1.2 - bug fix for non-ascii file names in encryption.xml
   0.1.3 - Try PyCrypto on Windows first
   0.1.4 - update zipfix to deal with mimetype not in correct place
   0.1.5 - update zipfix to deal with completely missing mimetype files
   0.1.6 - update to the new calibre plugin interface
   0.1.7 - Fix for potential problem with PyCrypto
   0.1.8 - an updated/modified zipfix.py and included zipfilerugged.py
   0.2.0 - Completely overhauled plugin configuration dialog and key management/storage
   0.2.1 - an updated/modified zipfix.py and included zipfilerugged.py
   0.2.2 - added in potential fixes from 0.1.7 that had been missed.
   0.2.3 - fixed possible output/unicode problem
   0.2.4 - ditched nearly hopeless caselessStrCmp method in favor of uStrCmp.
         - added ability to rename existing keys.
   0.2.5 - Major code change to use unaltered ignobleepub.py 3.6 and
         - ignoblekeygen 2.4 and later.
   0.2.6 - Modified to alleviate the issue with having both the ignoble and inept epub plugins installed/enabled
</pre>
</body>

</html>
