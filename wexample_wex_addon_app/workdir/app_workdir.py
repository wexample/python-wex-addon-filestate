from wexample_config.const.types import DictConfig
from wexample_filestate.const.disk import DiskItemType
from wexample_filestate_dev.workdir.mixins.with_readme_workdir_mixin import WithReadmeWorkdirMixin
from wexample_helpers.const.types import *

from wexample_wex_addon_app.const.globals import (
    APP_FILE_APP_CONFIG,
    APP_FILE_APP_ENV, APP_DIR_APP_DATA_NAME,
)
from wexample_wex_core.common.workdir import Workdir


class AppWorkdir(WithReadmeWorkdirMixin, Workdir):
    def prepare_value(self, config: Optional[DictConfig] = None) -> DictConfig:
        from wexample_config.config_value.filter.trim_config_value_filter import TrimConfigValueFilter

        config = super().prepare_value(config)

        config.update({
            "mode": "777",
            "mode_recursive": True,
        })

        children = config["children"]

        WithReadmeWorkdirMixin.append_readme(
            self,
            config=config
        )

        children.append({
            "name": 'version.txt',
            "type": DiskItemType.FILE,
            "should_exist": True,
            "default_content": f"0.0.1",
            "content_filter": TrimConfigValueFilter
        })

        children.append({
            "name": '.gitignore',
            "type": DiskItemType.FILE,
            "should_exist": True,
            "content_filter": TrimConfigValueFilter
        })

        children.append({
            "name": APP_DIR_APP_DATA_NAME,
            "type": DiskItemType.DIRECTORY,
            "should_exist": True,
            "children": [
                {
                    "name": APP_FILE_APP_ENV,
                    "type": DiskItemType.FILE,
                    "should_exist": True
                },
                {
                    "name": APP_FILE_APP_CONFIG,
                    "type": DiskItemType.FILE,
                    "should_exist": True
                },
                {
                    "name": "tmp",
                    "type": DiskItemType.DIRECTORY,
                    "should_exist": True
                }
            ]
        })

        return config
