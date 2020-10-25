#!/usr/bin/env python3
import re
import subprocess
# import sys

import osinfo
import oslogos


class InfoFetch(object):
    def __init__(self, os_name_id: str = None):
        # Configura a identidade do sistema operacional
        self.__os_name_id = os_name_id if os_name_id else osinfo.OsInfo().get_name_id()
        self.__os_logo = oslogos.Logo(os_name_id=self.__os_name_id)
        # Obtém as lista das linhas da logo e a lista das informações do sistema
        self.__logo_list = self.__os_logo.get_colored_ansi_code_as_list()
        self.__info_list = self.__get_system_info()
        # A barra de cor será acrescentada na menor lista
        self.__resolve_color_bar()

    @staticmethod
    def __illusion_float(logo_list: list, info_list: list, width_chars) -> list:
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
        if len(self.__info_list) <= len(self.__logo_list):
            self.__info_list.append(color_bar)
        else:
            self.__logo_list.append(color_bar)

    def __get_system_info(self) -> list:
        # Criar lista com informações do sistema
        os_info = osinfo.OsInfo()
        accent_color = self.__os_logo.get_accent_color()

        # Cabeçalho
        head = accent_color + os_info.get_username() + '@' + os_info.get_hostname() + '\033[m'
        len_head = len(head) - len(accent_color) - len('\033[m')
        head_base = '\033[m' + '-'*len_head

        # Nome do Sistema
        os_pretty_name = os_info.get_pretty_name()
        name = os_pretty_name if os_pretty_name else os_info.get_name() + '' + os_info.get_version()
        os_name = name + ' ' + os_info.get_codename()

        # Pacotes
        native_packages = os_info.get_packages()
        native_packages_manager = os_info.get_package_manager()
        flatpak_packages = os_info.get_flatpak_packages()
        snap_packages = os_info.get_snap_packages()
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
            packages_details = ' ({}{}{})'.format(native_packages_format, flatpak_packages_format, snap_packages_format)
        packages = total_packages + packages_details

        # Resto das informações
        architecture = os_info.get_architecture() + ' bits'
        kernel = os_info.get_kernel() + ' ' + os_info.get_kernel_version()
        motherboard = '{}, version:{}'.format(os_info.get_motherboard(), os_info.get_motherboard_version())
        cpu = os_info.get_cpu()
        gpu = os_info.get_gpu()
        ram = '{}, used {}, free {}'.format(os_info.get_ram(), os_info.get_ram_used(), os_info.get_ram_free())
        swap = '{}, used {}, free {}'.format(os_info.get_swap(), os_info.get_swap_used(), os_info.get_swap_free())
        resolution = os_info.get_screen_resolution()
        uptime = os_info.get_uptime()
        shell = os_info.get_shell()
        de = '{} {}'.format(os_info.get_desktop_environment(), os_info.get_desktop_environment_version())
        wm = os_info.get_window_manager()
        font = os_info.get_font()
        browser = os_info.get_browser()

        system_info_list = [
            head,
            head_base,
            accent_color + 'OS: ' + '\033[m' + os_name,
            accent_color + 'Architecture: ' + '\033[m' + architecture,
            accent_color + 'Kernel: ' + '\033[m' + kernel,
            accent_color + 'Board: ' + '\033[m' + motherboard,
            accent_color + 'CPU: ' + '\033[m' + cpu,
            accent_color + 'GPU: ' + '\033[m' + gpu,
            accent_color + 'RAM: ' + '\033[m' + ram,
            accent_color + 'Swap: ' + '\033[m' + swap,
            accent_color + 'Resolution: ' + '\033[m' + resolution,
            accent_color + 'Uptime: ' + '\033[m' + uptime,
            accent_color + 'Shell: ' + '\033[m' + shell,
            accent_color + 'DE: ' + '\033[m' + de,
            accent_color + 'WM: ' + '\033[m' + wm,
            accent_color + 'Packages: ' + '\033[m' + packages,
            accent_color + 'Font: ' + '\033[m' + font,
            accent_color + 'Browser: ' + '\033[m' + browser,
        ]

        # Falta verificar item nulo
        # ...

        return system_info_list

    def main(self) -> None:
        for i in self.__illusion_float(self.__logo_list, self.__info_list, 40):
            print(i)


if __name__ == '__main__':
    fetch = InfoFetch()
    fetch.main()
