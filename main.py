import hid

vid = 1267	# Change it for your device
pid = 1024	# Change it for your device
mouse = hid.Device(vid, pid)

while True:
    try:
        # Read a raw input report from the mouse
        raw_data = mouse.read(64, 10000)  # Adjust the buffer size as per your requirement
        
        # Process the raw data as needed
        print(raw_data)
    except KeyboardInterrupt:
        break
