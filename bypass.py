import os


def main() -> int:
    print("[~] Nuxt UI Pro license bypass by @qweme32\n")
    path = "./node_modules/@nuxt/ui-pro/modules/pro/license.ts"

    print("[*] Looking for license file at", path)
    if not os.path.exists(path):
        print(f"[-] License file not found at {path}")

        return 1
    
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()

    if "nuxt-ui-pro-license-bypass=true" in content:
        return 2
    
    print("[*] Replacing verify url to https://httpbin.org/status/200?nuxt-ui-pro-license-bypass=true")

    content = content.replace(
        "https://api.nuxtlabs.com/ui-pro/verify", 
        "https://httpbin.org/status/200?nuxt-ui-pro-license-bypass=true", 
    )

    with open(path, "w", encoding="utf-8") as file:
        file.write(content)
    
    return 0
    
    
if __name__ == "__main__":
    status = main()

    if status == 0:
        print("\n[+] License check bypassed")
    elif status == 2:
        print("\n[+] License check already bypassed")
    else:
        print("\n[-] Failed. Check logs")
