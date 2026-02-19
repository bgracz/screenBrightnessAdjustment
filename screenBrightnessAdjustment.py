import screen_brightness_control as sbc

def list_monitors():
    monitors = sbc.list_monitors()
    print("Available screens:")
    for i, name in enumerate(monitors):
        print(f"{name} - {i}")
    return list(range(len(monitors)))

def set_brightness_for_monitor(monitor_index, brightness):
    sbc.set_brightness(brightness, display=monitor_index)
    print(f"Brightness set to {brightness}% for screen {monitor_index}")

def set_brightness_for_all(brightness):
    monitors = list_monitors()
    for i in monitors:
        sbc.set_brightness(brightness, display=i)
    print(f"{brightness}% set for all screens")

def main():
    monitors = list_monitors()

    while True:
        user_input = input("\nInsert values (ex. 0 70), q to exit:").strip().lower()
        if user_input == 'q':
            break

        parts = user_input.split()
        if len(parts) != 2:
            print("Incorrect format")
            continue

        monitor_part, brightness_part = parts
        if brightness_part.isdigit():
            brightness = int(brightness_part)
            if not (0 <= brightness <= 100):
                print("Brightness must be in range 0-100")
                continue
            else:
                print("Brightness value must be a number")
                callable

            if monitor_part =='all':
                set_brightness_for_all(brightness)
            elif monitor_part.isdigit():
                monitor_index = int(monitor_part)
                if monitor_index in monitors:
                    set_brightness_for_monitor(monitor_index, brightness)
                else:
                    print("No screen with this id")
            else:
                print("Incorrect scrren id")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")