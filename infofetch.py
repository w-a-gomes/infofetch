#!/usr/bin/env python3
import re
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
            clean_line = re_color.sub('', line_logo)
            if len(clean_line) < width_chars:  # Contar quantos caracteres faltam na linha da logo para 'width_chars'
                missing_characters = width_chars - len(clean_line)
                line_logo = line_logo + ' '*missing_characters  # Acrescentar caracteres de espaços até preencher

            full_list.append(line_logo + ' ' + line_info)  # Linha completa para o 'print', usando lista da logo e info

        return full_list

    def __resolve_color_bar(self) -> None:
        # A barra de cor será acrescentada na menor lista
        color_bar = '\033[41m  \033[42m  \033[43m  \033[44m  \033[45m  \033[46m  \033[47m  \033[0m'
        if len(self.__info_list) <= len(self.__logo_list):
            self.__info_list.append(color_bar)
        else:
            self.__logo_list.append(color_bar)

    def __get_system_info(self) -> list:
        # Criar lista com informações do sistema
        accent_color = self.__os_logo.get_accent_color()
        os_info = osinfo.OsInfo()

        # Cabeçalho
        head = accent_color + os_info.get_username() + '@' + os_info.get_hostname() + '\033[m'
        head_base = '\033[m' + '-'*len(head)
        # Nome do Sistema
        os_pretty_name = os_info.get_pretty_name()
        name = os_pretty_name if os_pretty_name else os_info.get_name() + '' + os_info.get_version()
        os_name = name + ' ' + os_info.get_codename()
        # ...
        architecture = os_info.get_architecture() + ' bits'
        kernel = os_info.get_kernel() + ' ' + os_info.get_kernel_version()
        motherboard = '{}, version:{}'.format(os_info.get_motherboard(), os_info.get_motherboard_version())
        cpu = os_info.get_cpu()
        gpu = os_info.get_gpu()
        ram = '{}, used {}, free {}'.format(os_info.get_ram(), os_info.get_ram_used(), os_info.get_ram_free())

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
            accent_color + 'Swap: ' + '\033[m' + '',
            accent_color + 'Resolution: ' + '\033[m' + '',
            accent_color + 'Uptime: ' + '\033[m' + '',
            accent_color + 'Shell: ' + '\033[m' + '',
            accent_color + 'DE: ' + '\033[m' + '',
            accent_color + 'WM: ' + '\033[m' + '',
            accent_color + 'Packages: ' + '\033[m' + '',
            accent_color + 'Font: ' + '\033[m' + '',
            accent_color + 'Browser: ' + '\033[m' + '',
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
