from __future__ import annotations

from typing import TYPE_CHECKING

from wexample_wex_core.const.globals import COMMAND_TYPE_ADDON
from wexample_wex_core.decorator.command import command

if TYPE_CHECKING:
    from wexample_wex_core.context.execution_context import ExecutionContext


@command(
    type=COMMAND_TYPE_ADDON,
    description="Rollback the last applied migration on the current workdir",
)
def filestate__migration__rollback(context: ExecutionContext) -> None:
    from wexample_migration.workdir.mixin.with_migration_workdir_mixin import (
        WithMigrationWorkdirMixin,
    )

    workdir = context.kernel._call_workdir

    if not isinstance(workdir, WithMigrationWorkdirMixin):
        context.io.error(
            "Current workdir does not support migrations. "
            "Mix WithMigrationWorkdirMixin into your workdir class and override get_migrations()."
        )
        return

    rolled_back = workdir.migration_rollback()

    if rolled_back:
        context.io.success(f"Rolled back: {rolled_back}")
    else:
        context.io.log("Nothing to rollback.")
