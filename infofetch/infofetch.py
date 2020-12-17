#!/usr/bin/env python3
import re
import subprocess
import sys
import time

import osinfo
import oslogos


class InfoFetch(object):
    """Create an object of type 'InfoFetch'"""
    def __init__(self, os_name_id: str = None):
        """Class constructor"""
        # Configura a identidade do sistema operacional
        self.__os_info = osinfo.OsInfo()
        self.__os_name_id = os_name_id if os_name_id else self.__os_info.get_name_id()
        self.__os_logo = oslogos.Logo(os_name_id=self.__os_name_id)
        # Obtém as lista das linhas da logo e a lista das informações do sistema
        self.accent_color = self.__os_logo.get_accent_color()
        self.logo_as_list = self.__os_logo.get_colored_ansi_code_as_list()
        self.info_list = self.__get_system_info()
        # A barra de cor será acrescentada na menor lista
        self.__resolve_color_bar()

    @staticmethod
    def __illusion_float(logo_list: list, info_list: list, width_chars: int) -> list:
        # Garantir que a lista da esquerda (linhas da logo) fique com 'width_chars' (40) de tamanho.
        # Retorna uma lista em que cada linha é composta de 40 caracteres (width_chars) da linha da logo
        # e o resto da linha são informações do sistema.

        # Listas com a mesma quantidade de itens
        while len(logo_list) < len(info_list):
            logo_list.append(' ')
        while len(info_list) < len(logo_list):
            info_list.append(' ')

        full_list = list()  # Uma lista de linhas completas para exibir com 'print' será gerada
        for line_logo, line_info in zip(logo_list, info_list):
            re_color = re.compile(r'\x1b[^m]*m')  # Remover caracteres de cores invisíveis da contagem
            clean_line_logo = re_color.sub('', line_logo)
            clean_line_info = re_color.sub('', line_info)
            if len(clean_line_logo) < width_chars:  # Contar caracteres que faltam na linha da logo para 'width_chars'
                missing_characters = width_chars - len(clean_line_logo)
                line_logo = line_logo + ' '*missing_characters  # Acrescentar caracteres de espaços até preencher

            # Linha completa para o 'print', usando lista da logo e info
            full_line = line_logo + ' ' + line_info

            # Comparar tamanho da linha com o tamanho do terminal
            full_line_clean = clean_line_logo + ' ' + clean_line_info
            terminal_width = int(subprocess.getoutput('tput cols'))

            if len(full_line_clean) > terminal_width:
                remove = len(full_line_clean) - terminal_width
                full_line = full_line[:-remove]

            full_list.append(full_line)

        return full_list

    def __resolve_color_bar(self) -> None:
        # A barra de cor será acrescentada na menor lista
        color_bar = '\033[41m  \033[42m  \033[43m  \033[44m  \033[45m  \033[46m  \033[47m  \033[m'
        if len(self.info_list) <= len(self.logo_as_list):
            self.info_list.append(color_bar)
        else:
            self.logo_as_list.append(color_bar)

    def get_header(self) -> str:
        return self.accent_color + self.__os_info.get_username() + '@' + self.__os_info.get_hostname() + '\033[m'

    def get_header_decoration(self, header: str) -> str:
        len_header = len(header) - len(self.accent_color) - len('\033[m')
        return '\033[m' + '-' * len_header

    def get_os_name(self) -> str:
        os_pretty_name_ = self.__os_info.get_pretty_name()
        os_name_ = self.__os_info.get_name()
        name = os_pretty_name_ if os_pretty_name_ else os_name_ + '' + self.__os_info.get_version()
        os_name = name + ' ' + self.__os_info.get_codename()
        if not os_name and not os_pretty_name_:
            return 'unknown'
        return os_name

    def get_architecture(self) -> str:
        architecture = self.__os_info.get_architecture()
        return architecture + ' bits' if architecture else 'unknown'

    def get_kernel(self) -> str:
        kernel = self.__os_info.get_kernel()
        return kernel + ' ' + self.__os_info.get_kernel_version() if kernel else 'unknown'

    def get_motherboard(self) -> str:
        motherboard = self.__os_info.get_motherboard()
        motherboard_version = self.__os_info.get_motherboard_version()
        if motherboard and motherboard_version:
            return '{}, version {}'.format(motherboard, motherboard_version)
        elif motherboard and not motherboard_version:
            return motherboard
        else:
            return 'unknown'

    def get_cpu(self) -> str:
        cpu = self.__os_info.get_cpu()
        return cpu if cpu else 'unknown'

    def get_gpu(self) -> str:
        gpu = self.__os_info.get_gpu()
        return gpu if gpu else 'unknown'

    def get_ram(self) -> str:
        ram = self.__os_info.get_ram()
        return '{}, used {}, free {}'.format(
            ram, self.__os_info.get_ram_used(), self.__os_info.get_ram_free()) if ram else 'unknown'

    def get_swap(self) -> str:
        swap = self.__os_info.get_swap()
        return '{}, used {}, free {}'.format(
            swap, self.__os_info.get_swap_used(), self.__os_info.get_swap_free()) if swap else 'unknown'

    def get_resolution(self) -> str:
        resolution = self.__os_info.get_screen_resolution()
        return resolution if resolution else 'unknown'

    def get_uptime(self) -> str:
        uptime = self.__os_info.get_uptime()
        return uptime if uptime else 'unknown'

    def get_shell(self) -> str:
        shell = self.__os_info.get_shell()
        return shell if shell else 'unknown'

    def get_desktop_environment(self) -> str:
        get_de = self.__os_info.get_desktop_environment()
        get_de_version = self.__os_info.get_desktop_environment_version()
        de = get_de if get_de else ''
        de_version = get_de_version if get_de_version else ''
        if de_version:
            de = de + ' ' + de_version
        return de if de else 'unknown'

    def get_window_manager(self) -> str:
        wm = self.__os_info.get_window_manager()
        return wm if wm else 'unknown'

    def get_display_server(self):
        ds = self.__os_info.get_display_server()
        return ds if ds else 'unknown'

    def get_packages(self) -> str:
        native_packages = self.__os_info.get_packages()
        native_packages_manager = self.__os_info.get_package_manager()
        flatpak_packages = self.__os_info.get_flatpak_packages()
        snap_packages = self.__os_info.get_snap_packages()
        # Pacotes - variáveis de uso final
        total_packages = native_packages
        packages_details = ' - ' + native_packages_manager
        # Pacotes - Condição: Se houver flatpak ou snap
        if flatpak_packages or snap_packages:
            native_packages_format = '{}={}'.format(native_packages_manager, native_packages)
            flatpak_packages_format = ', flatpak={}'.format(flatpak_packages)
            snap_packages_format = ', snap={}'.format(snap_packages)
            # Variáveis de uso final
            total_packages = str(int(native_packages) + int(flatpak_packages) + int(snap_packages))
            packages_details = ' ({}{}{})'.format(
                native_packages_format, flatpak_packages_format, snap_packages_format)
        packages = total_packages + packages_details
        if not native_packages:
            packages = 'unknown'

        return packages

    def get_font(self) -> str:
        font = self.__os_info.get_font()
        return font if font else 'unknown'

    def get_browser(self) -> str:
        browser = self.__os_info.get_browser()
        return browser if browser else 'unknown'

    def __get_system_info(self) -> list:
        header = self.get_header()
        system_info_list = [
            header,
            self.get_header_decoration(header),
            self.accent_color + 'OS: ' + '\033[m' + self.get_os_name(),
            self.accent_color + 'Architecture: ' + '\033[m' + self.get_architecture(),
            self.accent_color + 'Kernel: ' + '\033[m' + self.get_kernel(),
            self.accent_color + 'Board: ' + '\033[m' + self.get_motherboard(),
            self.accent_color + 'CPU: ' + '\033[m' + self.get_cpu(),
            self.accent_color + 'GPU: ' + '\033[m' + self.get_gpu(),
            self.accent_color + 'RAM: ' + '\033[m' + self.get_ram(),
            self.accent_color + 'Swap: ' + '\033[m' + self.get_swap(),
            self.accent_color + 'Resolution: ' + '\033[m' + self.get_resolution(),
            self.accent_color + 'Uptime: ' + '\033[m' + self.get_uptime(),
            self.accent_color + 'Shell: ' + '\033[m' + self.get_shell(),
            self.accent_color + 'DE: ' + '\033[m' + self.get_desktop_environment(),
            self.accent_color + 'WM: ' + '\033[m' + self.get_window_manager(),
            self.accent_color + 'Display server: ' + '\033[m' + self.get_display_server(),
            self.accent_color + 'Packages: ' + '\033[m' + self.get_packages(),
            self.accent_color + 'Font: ' + '\033[m' + self.get_font(),
            self.accent_color + 'Default browser: ' + '\033[m' + self.get_browser(),
        ]

        # Remover informação indisponível
        for info in system_info_list:
            if info[-len('unknown'):] == 'unknown':
                system_info_list.remove(info)

        return system_info_list

    def main(self) -> None:
        """Shows system information

        Displays the system logo and system information.
        """
        for item in self.__illusion_float(self.logo_as_list, self.info_list, 40):
            print(item)


class Args(object):
    """Create an object of type 'Args'"""
    def __init__(self):
        """Class constructor

        Handles and executes the arguments that have been passed.
        """
        self.__exec_args()

    @staticmethod
    def __exec_args() -> None:
        # Verifica os argumentos e os exibe
        for arg in sys.argv:
            if '--help' in arg:
                help_text = (
                    '--help ┐\n ┌─────┘\n'
                    'Use:\n'
                    '  infofetch\n  infofetch [options]\n\n'
                    'The available options are:\n'
                    'OPTIONS                 DESCRIPTION\n'
                    '--help                  -Displays this help text\n'
                    '--list-supported-logos  -Displays a list with the name of the logos...\n'
                    '                         that are supported by this script\n'
                    '--show-all-logos        -Displays/draws on the screen all logos that...\n'
                    '                         are supported by this script'
                )
                print(help_text)
                print()
                continue

            elif '--list-supported-logos' in arg:
                print('--list-supported-logos ┐\n ┌─────────────────────┘')
                print(oslogos.Logo().get_list_of_supported_logos())
                print()
                continue

            elif '--show-all-logos' in arg:
                print('--show-all-logos ┐\n ┌───────────────┘')
                logo = oslogos.Logo()
                logo_list = logo.get_list_of_supported_logos()
                for ansi_logo in logo_list:
                    logo.set_os_name_id(ansi_logo)
                    print(ansi_logo)
                    print(logo.get_colored_ansi_code())
                    time.sleep(0.05)
                print()
                continue


if __name__ == '__main__':
    del(sys.argv[0])
    if sys.argv:
        args = Args()
    else:
        fetch = InfoFetch()
        fetch.main()
