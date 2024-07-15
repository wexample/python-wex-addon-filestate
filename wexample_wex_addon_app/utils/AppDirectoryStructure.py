from typing import Optional

from wexample_filestate.const.enums import DiskItemType
from wexample_filestate.const.types import StateItemConfig

from wexample_wex_addon_app.const.globals import (
    APP_FILE_APP_CONFIG,
    APP_FILE_APP_ENV,
)
from wexample_wex_core.utils.workdir import Workdir


class AppDirectoryStructure(Workdir):
    pass

    def build_setup_config(self, config: Optional[StateItemConfig] = None) -> StateItemConfig:
        config = super().build_setup_config(config)
        children = config["children"]

        children.append({
            "name": APP_FILE_APP_CONFIG,
            "type": DiskItemType.FILE,
            "should_exist": True
        })

        children.append({
            "name": APP_FILE_APP_ENV,
            "type": DiskItemType.DIRECTORY,
            "should_exist": True,
        })

        children.append({
            "name": "tmp",
            "type": DiskItemType.DIRECTORY,
            "should_exist": True
        })

        return config
