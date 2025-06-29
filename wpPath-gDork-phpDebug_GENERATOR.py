# Author: Nuriddin No'monov


wpPathGenerator = [
    "/wp-json/",
    "/wp-json/wp/v2/",
    "/wp-json/wp/v2/users",
    "/wp-json/wp/v2/posts",
    "/wp-json/wp/v2/pages",
    "/wp-json/wp/v2/comments",
    "/wp-json/wp/v2/media",
    "/wp-json/jwt-auth/v1/token",
    "/?rest_route=/wp/v2/users",
    "/wp-sitemap.xml",
    "/sitemap.xml",
    "/feed/",
    "/robots.txt",
    "/?author=1",
    "/author/admin/",
    "/wp-login.php",
    "/wp-admin/",
    "/wp-admin/admin-ajax.php",
    "/wp-content/uploads/",
    "/readme.html",
    "/license.txt"
]
wpExploit = [
    "/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php",
    "/wp-content/plugins/sexy-contact-form/includes/fileupload/index.php",
    "/wp-content/plugins/ajax-load-more/admin/admin.php",
    "/wp-content/plugins/revslider/temp/update_extract/revslider/",
    "/wp-admin/admin-post.php?page=revslider&action=update_plugin"
]

phpLaravelPaths = [
    "/.env",
    "/.git/config",
    "/.gitignore",
    "/composer.lock",
    "/composer.json",
    "/vendor/",
    "/vendor/autoload.php",
    "/server.php",
    "/routes/web.php",
    "/routes/api.php",
    "/storage/logs/laravel.log",
    "/storage/debugbar/",
    "/bootstrap/cache/",
    "/config/app.php",
    "/public/.htaccess",
    "/public/index.php",
    "/public/storage/",
    "/resources/views/errors/",
    "/resources/views/welcome.blade.php",
    "/_ignition/execute-solution",
    "/_ignition/health-check",
    "/_ignition/scripts/vendor/",
    "/_debugbar/open",
    "/_debugbar/assets/stylesheets",
    "/_debugbar/assets/javascript",
    "/phpinfo.php",
    "/info.php",
    "/debug.php",
    "/test.php",
    "/dev.php",
    "/x.php",
    "/p.php",
    "/config.php",
    "/backup.zip",
    "/backup.tar.gz",
    "/errors.log",
    "/logs/error.log",
    "/index.bak",
    "/index.php.bak"
]

admPageSearch = [
    "inurl:admin", "inurl:login", "inurl:dashboard",
    "intitle:'admin panel'", "intitle:'login'"
]
filesSearch = [
    "filetype:log", "filetype:txt", "filetype:sql",
    "filetype:env", "filetype:config", "filetype:bak"
]
vulnSearch = [
    "intext:error", "intext:warning", "intext:password",
    "intext:confidential", "inurl:debug", "inurl:backup"
]
indexSearch = [
    "intitle:'index of'", "intitle:'directory listing'", "intitle:'browse'"
]
techSearch = [
    "intext:'powered by'", "intext:'running on'", "intext:'version'", "inurl:version"
]

print("[$] Choose one of the following options:")

print("[1] WordPress Path Generator")
print("[2] Google Dork Generator")
print("[3] Laravel/PHP Debug Path List Generator")

mainChoice = input("[$] Enter your choice> ")


site = input("\n[$] Enter the domain> ")


if mainChoice == "1":
    print("""
[$] Select WordPress Path Category:
[1] wpPathGenerator
[2] wpExploit
    """)
    wpChoice = input("[$] Enter WordPress category> ")

    if wpChoice == "1":
        print("\n[$] WordPress Path Results:")
        for path in wpPathGenerator:
            print(f"{site}{path}")

    elif wpChoice == "2":
        print("\n[$] WordPress Exploit Paths:")
        for path in wpExploit:
            print(f"{site}{path}")
    else:
        print("[$] Wrong selection.")

elif mainChoice == "2":
    print("""
[$] Select Google Dork Category:
[1] Admin Page Search
[2] Vulnerability Search
[3] Files Search
[4] Index Pages Search
[5] Technology & Version Search
    """)
    dorkChoice = input("[$] Enter dork category> ")

    dorks = []

    if dorkChoice == "1":
        dorks = admPageSearch
    elif dorkChoice == "2":
        dorks = vulnSearch
    elif dorkChoice == "3":
        dorks = filesSearch
    elif dorkChoice == "4":
        dorks = indexSearch
    elif dorkChoice == "5":
        dorks = techSearch
    else:
        print("[$ Wrong selection")

    if dorks:
        print("\n[$] Google Dork Queries:")
        for dork in dorks:
            print(f"site:{site} {dork}")

elif mainChoice == "3":
    print("\n[$] Laravel/PHP Debug Paths:")
    for path in phpLaravelPaths:
        print(f"{site}{path}")


else:
    print("[$] Wrong choice!")
