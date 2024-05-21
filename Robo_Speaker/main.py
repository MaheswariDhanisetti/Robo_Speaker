import os

if __name__=='__main__':
    print("welcome to Robo Speaker 0.1 created by Mahi!")
    print("note:type 'q' to exit - ")
    command = f'powershell -Command "Add-Type –AssemblyName System.speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{"welcome to Robo Speaker"}\')"'
    os.system(command)
    while True:
        x=input("enter what you want me to pronounce : ")
        if x=='q':
            command = f'powershell -Command "Add-Type –AssemblyName System.speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{"Good Bye! Have a nice day."}\')"'
            os.system(command)
            break
        command=f'powershell -Command "Add-Type –AssemblyName System.speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')"'
        # command=f"say {x}" for mac
        os.system(command)


