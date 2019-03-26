#to enable these settings, name this file "user_settings.py"

user_settings = {
    #logs are saved to $HOME/steam-$STEAM_APP_ID.log, overwriting any previous log with that name
#     "WINEDEBUG": "", #"+timestamp,+pid,+tid,+seh,+debugstr,+module",

    #Disable nvapi and nvapi64
     "PROTON_NVAPI_DISABLE": "1",

    #Disable winedbg
     "PROTON_WINEDBG_DISABLE": "1",

    #Enable IMAGE_FILE_LARGE_ADDRESS_AWARE override - Required by some 32-bit games hitting address space issues
#     "PROTON_FORCE_LARGE_ADDRESS_AWARE": "1",

    #Reduce Pulse Latency
     "PROTON_PULSE_LOWLATENCY": "1",

    #Set DXVK logging level
#     "DXVK_LOG_LEVEL": "info",

    #Set DXVK custom config path
#     "DXVK_CONFIG_FILE": "",

    #Enable DXVK Async pipecompiler
#     "PROTON_DXVK_ASYNC": "1",

    #Enable DXVK's HUD
#     "DXVK_HUD": "devinfo,fps",

    #Use gl-based wined3d for d3d11 and d3d10 instead of vulkan-based dxvk !!! Won't affect DXVK winelib builds !!!
#     "PROTON_USE_WINED3D": "1",

    #Disable d3d11 entirely !!! Won't affect DXVK winelib builds !!!
#     "PROTON_NO_D3D11": "1",

    #Disable in-process synchronization primitives
#     "PROTON_NO_ESYNC": "1",
}
