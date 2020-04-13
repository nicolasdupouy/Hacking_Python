# pip install pybluez


import platform
import os
import time
import bluetooth


def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("clear")


class BluetoothScanner:
    log_messages = []
    found_devices = {}
    update_display_required = False

    def update_discoverable_devices(self):
        devices = bluetooth.discover_devices(lookup_names=True)
        for (addr, name) in devices:
            if addr not in self.found_devices:
                self.add_found_device(addr, name)

        for (addr, name) in self.found_devices.copy().items():
            if (addr, name) not in devices:
                self.remove_lost_device(addr, name)

    def add_found_device(self, addr, name):
        self.log_messages.append('[*] Found Bluetooth Device: {} / [+] MAC address: {}'.format(str(name), str(addr)))
        self.found_devices[addr] = name
        self.update_display_required = True

    def remove_lost_device(self, addr, name):
        self.log_messages.append('[*] Lost Bluetooth Device: {} / [+] MAC address: {}'.format(str(name), str(addr)))
        del self.found_devices[addr]
        self.update_display_required = True

    def display_discovered_devices(self):
        if self.update_display_required: # self.found_devices and
            clear_screen()
            for log_message in self.log_messages:
                print(log_message)

            print('\n')
            print('#####################################################################')
            print('## Discoverable Bluetooth devices ###################################')
            print('#####################################################################')
            for (addr, name) in self.found_devices.items():
                print('MAC Address: {} / Name: {}'.format(str(addr), str(name)))
            print('#####################################################################')

            self.update_display_required = False


if __name__ == '__main__':
    bluetooth_scanner = BluetoothScanner()
    while True:
        bluetooth_scanner.update_discoverable_devices()
        bluetooth_scanner.display_discovered_devices()
        time.sleep(1)