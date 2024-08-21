# Nuxt UI Pro Bypass

**The repository exists only to show the problem do not use this script in production !!!**

Instruction
1. Place bypass.py into your repository with nuxt-ui-pro template
    ```
    Project structure
    - .nuxt
    - app
    - content
    - node_modules
    - public
    - server
    .env
    bypass.py <---
    and other files...
    ```
2. Install packages via npm
    ```
    npm i
    ```
3. Create .env file with content
    ```
    # Production license for @nuxt/ui-pro, get one at https://ui.nuxt.com/pro/purchase
    NUXT_UI_PRO_LICENSE=any-string
    ```
4. Run python script
    ```
    python3 bypass.py
    ```
    
