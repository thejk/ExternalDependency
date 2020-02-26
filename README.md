# ExternalDependency

Sample project for a bug where Android Studio asks gradle to download POM files
for local file dependencies.

To reproduce:
1) Clone this repo
2) Run trivial http_server to see bad requests
   python3 http_server.py
3) Import project in Android Studio

During Gradle sync (and every following sync) note output from http_server.py:
Bad request: /__local_aars__/full/path/external/external.jar/unspecified/full/path/external/external.jar-unspecified.pom

This means that every repository in the project just got a request for
a pom file that will never exist.