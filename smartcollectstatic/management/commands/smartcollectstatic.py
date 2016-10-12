from __future__ import unicode_literals

from os.path import abspath

from django.contrib.staticfiles.management.commands.collectstatic import Command as BaseCommand  # noqa
from django.core.management.base import CommandError
from django.conf import settings


class Command(BaseCommand):
    def link_or_copy_file(self, path, prefixed_path, source_storage):
        source_path = source_storage.path(path)
        is_in_project = source_path.startswith(self.__base_path)
        if is_in_project:
            return self.__link_file(path, prefixed_path, source_storage)
        return self.__copy_file(path, prefixed_path, source_storage)

    def collect(self):
        if not self.symlink:
            raise CommandError(
                "Can't use smart collectstatc without symlink option")

        self.__link_file = self.link_file
        self.__copy_file = self.copy_file
        self.__base_path = abspath(settings.BASE_DIR)
        self.link_file = self.link_or_copy_file
        self.copy_file = self.link_or_copy_file
        return super().collect()
