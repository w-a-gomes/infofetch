#!/usr/bin/env python3
# https://github.com/w-a-gomes/systemutils
import subprocess
import re


class OsInfo(object):
    """Create an object of type 'OsInfo'

    Gets information about the operating system.
    """
    def __init__(self):
        """Class constructor"""
        self.__user = str()
        self.__username = str()
        self.__hostname = str()
        self.__all_release_info = dict()
        self.__pretty_name = str()
        self.__name = str()
        self.__name_id = str()
        self.__codename = str()
        self.__version = str()
        self.__kernel = str()
        self.__kernel_version = str()
        self.__architecture = str()
        self.__motherboard = str()
        self.__motherboard_version = str()
        self.__cpu = str()
        self.__gpu = str()
        self.__ram = str()
        self.__ram_used = str()
        self.__ram_free = str()
        self.__swap = str()
        self.__swap_used = str()
        self.__swap_free = str()
        self.__screen_resolution = str()
        self.__uptime = str()
        self.__shell = str()
        self.__desktop_environment = str()
        self.__desktop_environment_version = str()
        self.__window_manager = str()
        self.__package_manager = str()
        self.__display_server = str()
        self.__packages = str()
        self.__flatpak_packages = str()
        self.__snap_packages = str()
        self.__font = str()
        self.__browser = str()

    def get_user(self) -> str:
        """The user name

        The correct name that the user registered, not the 'username'.

        :return: String containing the user name
        """
        if self.__user:
            return self.__user

        self.__user = subprocess.getoutput(
            "cat /etc/passwd | grep `whoami` | awk -F ',' '{print $1}' | awk -F ':' '{print $5}'")

        return self.__user

    def get_username(self) -> str:
        """The username

        The username used to log in, not the correct or correctly formatted name.

        :return: String containing username
        """
        if self.__username:
            return self.__username

        self.__username = subprocess.getoutput('echo $USER')
        return self.__username

    def get_hostname(self) -> str:
        """The host name

        The recognition name on the network.

        :return: String containing the hostname
        """
        if self.__hostname:
            return self.__hostname

        # Fix $HOSTNAME missing
        if subprocess.getoutput('cat /etc/hostname ; echo $?')[-1] == '0':
            hostname = subprocess.getoutput('cat /etc/hostname')
        else:
            hostname = subprocess.getoutput('echo $HOSTNAME')

        # Fix $HOSTNAME in Fedora
        if 'fedora' in self.get_name().lower():
            hostname = subprocess.getoutput('printf "${HOSTNAME%%.*}"')

        self.__hostname = hostname
        return self.__hostname

    def get_all_release_info(self) -> dict:
        """cat /etc/os-release

        All information from the '/etc/os-release' file in a dictionary.

        :return: Dict containing information from the '/etc/os-release' file
        """
        if self.__all_release_info:
            return self.__all_release_info

        # Return var
        all_release_info = dict()

        cat_release = subprocess.getoutput('cat /etc/os-release').split('\n')
        for item_release in cat_release:
            items = item_release.split('=')
            all_release_info[items[0]] = items[1].strip('"').strip("'")

        # HACK: Identify some known distributions that do not configure version information as they should
        hack_name = False
        name = str()
        name_id = str()

        if 'ubuntu' in all_release_info['NAME'].lower():
            # Lubuntu
            if 'openbox' in subprocess.getoutput('ls /usr/share/lubuntu/'):
                hack_name = True
                name = 'Lubuntu'
                name_id = 'lubuntu'

            # ubuntu Budgie
            elif 'Budgie Welcome' in subprocess.getoutput('ubuntu-budgie-welcome.budgie-welcome --version'):
                hack_name = True
                name = 'Ubuntu Budgie'
                name_id = 'ubuntubudgie'

            # Xubuntu
            elif 'applications' in subprocess.getoutput('ls /usr/share/xubuntu/'):
                hack_name = True
                name = 'Xubuntu'
                name_id = 'xubuntu'

        if hack_name:
            all_release_info['NAME'] = name
            all_release_info['ID'] = name_id
            if 'PRETTY_NAME' in all_release_info:
                all_release_info['PRETTY_NAME'] = all_release_info['PRETTY_NAME'].replace('Ubuntu', name)

        self.__all_release_info = all_release_info
        return self.__all_release_info

    def get_pretty_name(self) -> str:
        """Verbally formatted name

        The pretty name in the '/etc/os-release' file.

        :return: String containing pretty name
        """
        if self.__pretty_name:
            return self.__pretty_name

        if not self.__all_release_info:
            self.get_all_release_info()

        if 'PRETTY_NAME' in self.__all_release_info:
            self.__pretty_name = self.__all_release_info['PRETTY_NAME']

        return self.__pretty_name

    def get_name(self) -> str:
        """Operating system name

        The commercially formatted name, which can contain uppercase letters and spaces.

        :return: String containing the name of the operating system
        """
        if self.__name:
            return self.__name

        if not self.__all_release_info:
            self.get_all_release_info()

        if 'NAME' in self.__all_release_info:
            self.__name = self.__all_release_info['NAME']
        return self.__name

    def get_name_id(self) -> str:
        """Operating system identity

        The identifier formatted name for code or database; usually in lowercase and without spaces.

        :return: String containing the operating system ID
        """
        if self.__name_id:
            return self.__name_id

        if not self.__all_release_info:
            self.get_all_release_info()

        if 'ID' in self.__all_release_info:
            self.__name_id = self.__all_release_info['ID']
        elif 'NAME' in self.__all_release_info:
            self.__name_id = self.__all_release_info['NAME'].lower()

        return self.__name_id

    def get_codename(self) -> str:
        """Operating system codename

        The code name is the commercial one, to easily identify the versions of the operating system.
        Not all systems do.

        :return: String containing the codename of the operating system
        """
        if self.__codename:
            return self.__codename

        if not self.__all_release_info:
            self.get_all_release_info()

        if 'VERSION_CODENAME' in self.__all_release_info:
            self.__codename = self.__all_release_info['VERSION_CODENAME']
        elif 'CODENAME' in self.__all_release_info:
            self.__codename = self.__all_release_info['CODENAME']

        return self.__codename

    def get_version(self) -> str:
        """Operating system version

        The current version of the operating system.

        :return: String containing the version of the operating system
        """
        if self.__version:
            return self.__version

        if not self.__all_release_info:
            self.get_all_release_info()

        if 'VERSION_ID' in self.__all_release_info:
            self.__version = self.__all_release_info['VERSION_ID']
        elif 'VERSION' in self.__all_release_info:
            self.__version = self.__all_release_info['VERSION']

        return self.__version

    def get_kernel(self) -> str:
        """Operating system kernel name

        The current operating system kernel.

        :return: String containing the kernel name
        """
        if self.__kernel:
            return self.__kernel

        self.__kernel = subprocess.getoutput('cat /proc/sys/kernel/ostype').title()
        return self.__kernel

    def get_kernel_version(self) -> str:
        """Operating system kernel version

        The current kernel version of the operating system.

        :return: String containing the kernel version
        """
        if self.__kernel_version:
            return self.__kernel_version

        regex = re.compile(r'(\.x\d.+|x\d.+)')
        self.__kernel_version = regex.sub(
            '', subprocess.getoutput('cat /proc/sys/kernel/osrelease'))

        return self.__kernel_version

    def get_architecture(self) -> str:
        """

        :return:
        """
        if self.__architecture:
            return self.__architecture

        self.__architecture = subprocess.getoutput('getconf LONG_BIT').title()
        return self.__architecture

    def get_motherboard(self) -> str:
        """

        :return:
        """
        if self.__motherboard:
            return self.__motherboard

        self.__motherboard = subprocess.getoutput(
            'cat /sys/devices/virtual/dmi/id/product_name')
        return self.__motherboard

    def get_motherboard_version(self) -> str:
        """

        :return:
        """
        if self.__motherboard_version:
            return self.__motherboard_version

        self.__motherboard_version = subprocess.getoutput(
            'cat /sys/devices/virtual/dmi/id/product_version')
        return self.__motherboard_version

    def get_cpu(self) -> str:
        """

        :return:
        """
        if self.__cpu:
            return self.__cpu
        self.__cpu = subprocess.getoutput(
            "cat /proc/cpuinfo | grep 'model name' | sed -n 1p | sed 's/.*:.//g;s/(.*)//g'")
        return self.__cpu

    def get_gpu(self) -> str:
        """

        :return:
        """
        if self.__gpu:
            return self.__gpu

        gpu_id = subprocess.getoutput("lspci |grep -i graphics|awk '{ print $1 }'")
        gpu_label = str()

        if gpu_id.replace(':', '').replace('.', '').isdigit():
            gpu_label = subprocess.getoutput(
                'cat "/sys/bus/pci/devices/0000:{}/label"'.format(gpu_id)).strip()
            if 'cat: ' in gpu_label:
                gpu_label = ''

        gpu_read = subprocess.getoutput('lspci | grep VGA')
        if 'lspci:' in gpu_read or '/bin/sh:' in gpu_read:
            return gpu_label

        regex = re.findall(r'.+: (.+)', gpu_read)
        gpu = str()
        if regex:
            gpu = regex[0]

        regex_to_remove = re.findall(r'\(.+\)', gpu_read)
        if regex_to_remove:
            gpu = gpu.replace(regex_to_remove[0], '')

        if 'intel' in gpu.lower():
            dirt_to_clean = ['Corporation', 'Core Processor', 'Integrated Graphics Controller']
            for i in dirt_to_clean:
                gpu = gpu.replace(i, '')

        if 'virtualbox' in gpu.lower():
            gpu = 'VirtualBox Graphics Adapter'

        self.__gpu = '{}{}'.format(gpu.replace('  ', ' '), gpu_label).strip()
        return self.__gpu

    def get_ram(self) -> str:
        """

        :return:
        """
        if self.__ram:
            return self.__ram
        # Somente um método pega todas as informações das memórias
        # para evitar repetir o comando do shell

        # Pegar linhas da memória ram e swap
        memory_info = subprocess.getoutput("free -h").replace(',', '.').split('\n')
        ram_line = memory_info[1].split(' ')  # memory_info[0] é o cabeçalho
        swap_line = memory_info[2].split(' ')

        # Lista para armazenar as informações das memórias ram e swap
        ram_info = list()
        swap_info = list()

        # Preencher as lista com caracteres válidos, removendo caracteres vazios
        for ram in ram_line:
            if ram != '':
                ram_info.append(ram)
        for swap in swap_line:
            if swap != '':
                swap_info.append(swap)

        # Atribuir valores da memória ram
        self.__ram = ram_info[1]
        self.__ram_used = ram_info[2]
        self.__ram_free = ram_info[3]
        # Atribuir valores da memória swap
        self.__swap = swap_info[1]
        self.__swap_used = swap_info[2]
        self.__swap_free = swap_info[3]

        return self.__ram

    def get_ram_used(self) -> str:
        """

        :return:
        """
        if self.__ram_used:
            return self.__ram_used

        self.get_ram()
        return self.__ram_used

    def get_ram_free(self) -> str:
        """

        :return:
        """
        if self.__ram_free:
            return self.__ram_free

        self.get_ram()
        return self.__ram_free

    def get_swap(self) -> str:
        """

        :return:
        """
        if self.__swap:
            return self.__swap

        self.get_ram()
        return self.__swap

    def get_swap_used(self) -> str:
        """

        :return:
        """
        if self.__swap_used:
            return self.__swap_used

        self.get_ram()
        return self.__swap_used

    def get_swap_free(self) -> str:
        """

        :return:
        """
        if self.__swap_free:
            return self.__swap_free

        self.get_ram()
        return self.__swap_free

    def get_screen_resolution(self) -> str:
        """

        :return:
        """
        if self.__screen_resolution:
            return self.__screen_resolution

        if subprocess.getoutput('xrandr ; echo $?')[-1] == '0':
            resolution = subprocess.getoutput(
                "xrandr | grep current | awk -F , '{print $2}'")
            self.__screen_resolution = resolution.replace(' current ', '').replace(' x ', 'x')

        return self.__screen_resolution

    def get_uptime(self) -> str:
        """

        :return:
        """
        if self.__uptime:
            return self.__uptime

        uptime = subprocess.getoutput('uptime -p')
        if uptime[:7] == 'uptime:':
            self.__uptime = subprocess.getoutput('uptime').split(',')[0][9:].replace('up', '').strip() + ' Hs'
        else:
            self.__uptime = uptime.replace('up ', '')

        return self.__uptime

    def get_shell(self) -> str:
        """

        :return:
        """
        if self.__shell:
            return self.__shell

        self.__shell = subprocess.getoutput('basename $SHELL')
        return self.__shell

    def get_desktop_environment(self) -> str:
        """

        :return:
        """
        if self.__desktop_environment:
            return self.__desktop_environment

        desktop_environment = subprocess.getoutput(
            'echo $XDG_CURRENT_DESKTOP').replace(':', '-').strip()

        # Limpar
        dirt_to_clean = ['(', ')', "'", '"', 'X-']
        for cleaning_item in dirt_to_clean:
            self.__desktop_environment = desktop_environment.replace(cleaning_item, '')

        # Customizar
        if 'kde' in self.__desktop_environment.lower():
            self.__desktop_environment = 'Plasma (KDE)'

        return self.__desktop_environment

    def get_desktop_environment_version(self) -> str:
        """

        :return:
        """
        if self.__desktop_environment_version:
            return self.__desktop_environment_version

        cmd_version = {
            # 'budgie': "budgie-desktop --version | awk '{print $2}'",
            'cinnamon': "cinnamon --version | awk '{print $2}'",
            # deepin
            'gnome': "gnome-shell --version | awk '{print $3}'",
            'kde': "plasmashell --version | awk '{print $2}'",
            # lxde
            'lxqt': "lxqt-about -v | grep liblxqt | awk '{print $2}'",
            # pantheon elementary
            'xfce': "xfce4-about -V | grep xfce4-about | awk '{print $2}'",
        }
        de = self.get_desktop_environment().lower()
        desktop_environment_version = str()
        for cmd_version_key, cmd_version_value in cmd_version.items():
            if cmd_version_key in de:
                desktop_environment_version = subprocess.getoutput(cmd_version_value)
                break

        # Limpar
        dirt_to_clean = ['(', ')', "'", '"', 'X-']
        for cleaning_item in dirt_to_clean:
            self.__desktop_environment_version = desktop_environment_version.replace(cleaning_item, '')

        # Customizar
        error = ['bash: ', '/bin/sh: ']
        for item_error in error:
            if item_error in self.__desktop_environment_version.lower():
                self.__desktop_environment_version = ''
                break

        return self.__desktop_environment_version

    def get_window_manager(self) -> str:
        """

        :return:
        """
        if self.__window_manager:
            return self.__window_manager

        cmd_xprop = subprocess.getoutput('xprop -root -notype _NET_SUPPORTING_WM_CHECK')
        cmd_window_manager = subprocess.getoutput(
            'xprop -id {} -notype -len 100 -f _NET_WM_NAME 8t | grep WM_KEY'.format(
                cmd_xprop.split()[-1])).split('=')[-1].replace('"', '').strip()

        if cmd_window_manager == '':
            cmd_xprop = subprocess.getoutput('xprop -root -notype _NET_SUPPORTING_WM_CHECK')
            cmd_window_manager = subprocess.getoutput(
                'xprop -id {} -notype -len 100 -f _NET_WM_NAME 8t | grep WM_NAME'.format(
                    cmd_xprop.split()[-1])).split('=')[-1].replace('"', '').strip()

        self.__window_manager = cmd_window_manager.replace(',', ' | ').replace('(', '').replace(')', '')
        if 'xprop:' in cmd_window_manager:
            self.__window_manager = ''

        return self.__window_manager

    def get_display_server(self) -> str:
        """

        :return:
        """
        if self.__display_server:
            return self.__display_server

        self.__display_server = subprocess.getoutput('echo $XDG_SESSION_TYPE')
        return self.__display_server

    def get_package_manager(self) -> str:
        """

        :return:
        """
        if self.__package_manager:
            return self.__package_manager

        cmd_packages = {
            'dpkg': 'dpkg --get-selections | grep -cv deinstall$',
            'rpm': 'rpm -qa | wc -l',
            'pacman': 'pacman -Qq --color never | wc -l',
            'eopkg': 'eopkg list-installed | wc -l',
        }

        for cmd_packages_key, cmd_packages_value in cmd_packages.items():
            number = int(subprocess.getoutput(cmd_packages_value).split()[-1])

            if number > 0:
                self.__package_manager = cmd_packages_key
                self.__packages = str(number)

        return self.__package_manager

    def get_packages(self) -> str:
        """

        :return:
        """
        if self.__packages:
            return self.__packages

        self.get_package_manager()

        return self.__packages

    def get_flatpak_packages(self) -> str:
        """

        :return:
        """
        if self.__flatpak_packages:
            return self.__flatpak_packages

        number = int(subprocess.getoutput('flatpak list | wc -l').split()[-1])
        if number > 0:
            self.__flatpak_packages = str(number)

        return self.__flatpak_packages

    def get_snap_packages(self) -> str:
        """

        :return:
        """
        if self.__snap_packages:
            return self.__snap_packages

        # Remove cabeçalho com: grep -v "^Name"
        # number = int(subprocess.getoutput('snap list | grep -v "^Name" | wc -l').split()[-1])

        # Remove cabeçalho com '-1' no fim
        number = int(subprocess.getoutput('snap list | wc -l').split()[-1]) - 1
        if number > 0:
            self.__snap_packages = str(number)

        return self.__snap_packages

    def get_font(self) -> str:
        """

        :return:
        """
        if self.__font:
            return self.__font

        self.__font = re.findall(r':.(.+)', subprocess.getoutput('fc-match'))[0].replace('"', '')
        return self.__font

    def get_browser(self) -> str:
        """

        :return:
        """
        if self.__browser:
            return self.__browser

        desktop_file = subprocess.getoutput('xdg-settings get default-web-browser').lower()
        browser = desktop_file.replace('.desktop', '').replace('-', ' ')
        bad_list = [
            '/bin/sh:', 'xdg-settings:', 'leafpad', 'kwrite', 'gedit', 'kate', 'debian', 'sensible']
        for bad_item in bad_list:
            if bad_item in browser:
                browser = ''

        if '.' in browser:
            regex_browser = re.findall(r'\.(\w+$)', browser)
            if regex_browser:
                browser = regex_browser[0]

        browser = '' if browser == ' ' else browser
        self.__browser = browser.title()

        return self.__browser


if __name__ == '__main__':
    oi = OsInfo()
    print('                       user:', oi.get_user())
    print('                   username:', oi.get_username())
    print('                   hostname:', oi.get_hostname())
    print('                pretty-name:', oi.get_pretty_name())
    print('                       name:', oi.get_name())
    print('                    name-id:', oi.get_name_id())
    print('                   codename:', oi.get_codename())
    print('                    version:', oi.get_version())
    print('                     kernel:', oi.get_kernel())
    print('             kernel-version:', oi.get_kernel_version())
    print('               architecture:', oi.get_architecture())
    print('                motherboard:', oi.get_motherboard())
    print('        motherboard-version:', oi.get_motherboard_version())
    print('                        cpu:', oi.get_cpu())
    print('                        gpu:', oi.get_gpu())
    print('                        ram:', oi.get_ram())
    print('                   ram-used:', oi.get_ram_used())
    print('                   ram-free:', oi.get_ram_free())
    print('                       swap:', oi.get_swap())
    print('                  swap-used:', oi.get_swap_used())
    print('                  swap-free:', oi.get_swap_free())
    print('          screen-resolution:', oi.get_screen_resolution())
    print('                     uptime:', oi.get_uptime())
    print('                      shell:', oi.get_shell())
    print('        desktop-environment:', oi.get_desktop_environment())
    print('desktop-environment-version:', oi.get_desktop_environment_version())
    print('             window-manager:', oi.get_window_manager())
    print('             display-server:', oi.get_display_server())
    print('            package-manager:', oi.get_package_manager())
    print('                   packages:', oi.get_packages())
    print('           flatpak-packages:', oi.get_flatpak_packages())
    print('              snap-packages:', oi.get_snap_packages())
    print('                       font:', oi.get_font())
    print('                    browser:', oi.get_browser())
    r = oi.get_all_release_info()
    for k, v in r.items():
        print(k, '=', v)
