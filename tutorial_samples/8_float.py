def main():
    OnFwd(OUT_AC, 75)
    Wait(500)
    Off(OUT_AC)
    Wait(1000)
    OnFwd(OUT_AC, 75)
    Wait(500)
    Coast(OUT_AC)