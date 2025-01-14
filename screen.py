import screen_brightness_control as sbc
import time

def adjust_brightness():
    while True:
        try:
            # Get current brightness
            current = sbc.get_brightness()[0]
            print(f"Current brightness: {current}%")
            
            # Get user input
            new_brightness = int(input("Enter brightness level (0-100) or -1 to exit: "))
            
            # Exit condition
            if new_brightness == -1:
                break
                
            # Validate input
            if 0 <= new_brightness <= 100:
                sbc.set_brightness(new_brightness)
                print(f"Brightness set to {new_brightness}%")
            else:
                print("Please enter a value between 0 and 100")
                
        except ValueError:
            print("Please enter a valid number")
        except Exception as e:
            print(f"An error occurred: {e}")
            break
            
        time.sleep(0.5)  # Small delay to prevent excessive updates

if __name__ == "__main__":
    print("Screen Brightness Control")
    print("------------------------")
    adjust_brightness()
