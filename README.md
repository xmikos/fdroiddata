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

- [https://eutopia.cz/fdroid/repo](https://eutopia.cz/fdroid/repo?fingerprint=A0E4D1D912D8B81809AB18F5B7CF562CD1A10533ED4F7B25E595ABC8D862AD87)

You can also add archive repository (which contains older versions of applications
from the main repository):

- [https://eutopia.cz/fdroid/archive](https://eutopia.cz/fdroid/archive?fingerprint=A0E4D1D912D8B81809AB18F5B7CF562CD1A10533ED4F7B25E595ABC8D862AD87)

There is also experimental repository, where you will find only WebSocket-based fork
of TextSecure for now:

- [https://eutopia.cz/experimental/fdroid/repo](https://eutopia.cz/experimental/fdroid/repo?fingerprint=A0E4D1D912D8B81809AB18F5B7CF562CD1A10533ED4F7B25E595ABC8D862AD87)

Motivation
----------

My primary motivation for creating this repository has been the absence of [TextSecure](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms)
private messenger from the official F-Droid repository. TextSecure has already been included in
F-Droid for a brief time in the past, but Moxie Marlinspike (author of TextSecure) didn't like
this and demanded it to be removed. TextSecure is Free Software (licensed under GPL), so F-Droid
maintainers didn't have to remove it, but nevertheless they did.

There has been big discussion about it (issue [#127](https://github.com/WhisperSystems/TextSecure/issues/127)),
but simply told, Moxie is not open to arguments and wants TextSecure to be distributed only via
Google Play. He already locked this discussion. This is unacceptable for me, because applications
installed from Google Play can be silently updated without user knowing about it, e.g. to version
with hidden backdoor.

TextSecure still needs Google Play Services (because it uses [Google Cloud Messaging](https://developers.google.com/cloud-messaging/)),
but you don't need Google Account and Google Play cannot silently update app that has been
installed outside of Google Play store. Hopefully in the future, it will be possible to use
official TextSecure client without Google Play Services (see issue [#1000](https://github.com/WhisperSystems/TextSecure/issues/1000) - 
Websocket support, unfortunately Moxie also locked this discussion). For now there is unofficial
[TextSecure fork](https://github.com/JavaJens/TextSecure) by JavaJens, which already uses
WebSocket instead of GCM and therefore doesn't need Google Play Services. You can install it
from my experimental F-Droid repository.
