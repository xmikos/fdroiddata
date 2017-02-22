Eutopia.cz F-Droid Repository
=============================

The official [F-Droid](https://f-droid.org) app repository of the [Eutopia.cz](https://eutopia.cz)
website. Applications in this repository are built directly from the source code.

**Webpage:** https://fdroid.eutopia.cz

Usage
-----

First install [F-Droid](https://f-droid.org) (app store for Free and Open Source Software)
on your Android device. Then add this repository to F-Droid (click on the link below in web browser
on Android and select F-Droid from the list of apps):

- **[https://eutopia.cz/fdroid/repo](https://eutopia.cz/fdroid/repo?fingerprint=A0E4D1D912D8B81809AB18F5B7CF562CD1A10533ED4F7B25E595ABC8D862AD87)**

What is LibreSignal?
--------------------

LibreSignal is independent build of excellent [Signal](https://whispersystems.org) private messenger
by Open Whisper Systems. It is built from official source code, only renamed to LibreSignal.

Why have Signal been renamed to LibreSignal?
--------------------------------------------

Moxie Marlinspike (author of Signal) apparently doesn't like the idea of independent builds of Signal so much,
that he started with legal threats on Twitter. Independent builds of Signal have been therefore renamed to LibreSignal.

Application ID is still the same, so you will not lose data after upgrade.

Can I switch from Signal to LibreSignal without losing data?
------------------------------------------------------------

LibreSignal builds are signed with different key than official Signal builds. First you have to uninstall
official Signal app and then install LibreSignal. But by uninstalling Signal, you will lose app data
(most importantly your private encryption keys). There has been option in TextSecure (Signal predecessor)
to export encrypted backup in the past, but it has been removed (because of issues with it) and never brought back.

One possible solution (if you have root access on your device) is to use [oandbackup](https://f-droid.org/repository/browse/?fdfilter=oandbackup&fdid=dk.jens.backup).
Backup your Signal app data with oandbackup, uninstall Signal, install LibreSignal and restore your backup with oandbackup.

Does LibreSignal work without Google Play Services?
---------------------------------------------------

There has been experimental repository with WebSocket fork of LibreSignal in the past. But starting
with LibreSignal version 3.30.0, it is not needed anymore. Official Signal (and therefore LibreSignal) now
finally works without Google Play Services too.

If you want also encrypted voice and video calls to work without Google Play Services, both you and the other side
have to enable *Video calling beta* option in *Settings -> Advanced*.
See [Video calls for Signal now in public beta](https://whispersystems.org/blog/signal-video-calls-beta) for more information.

Motivation
----------

My primary motivation for creating this repository has been the absence of
[TextSecure](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms)
private messenger (Signal predecessor) from the official F-Droid repository. TextSecure has already been included in F-Droid for
a brief time in the past, but Moxie Marlinspike (author of TextSecure) didn't like it and demanded it to be
removed. TextSecure is Free Software (licensed under GPL), so F-Droid maintainers didn't have to remove it,
but nevertheless they did.

There has been big discussion about it
(issue [#127](https://github.com/WhisperSystems/TextSecure/issues/127)), but simply told, Moxie
has not been open to arguments and wanted TextSecure to be distributed only via Google Play. He already locked this
discussion. This has been unacceptable for me, because applications installed from Google Play can be silently
updated without user knowing about it, e.g. to version with hidden backdoor.
