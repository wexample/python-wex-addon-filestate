from __future__ import annotations

from typing import TYPE_CHECKING

from wexample_wex_core.const.globals import COMMAND_TYPE_ADDON
from wexample_wex_core.decorator.command import command

if TYPE_CHECKING:
    from wexample_wex_core.context.execution_context import ExecutionContext


@command(
    type=COMMAND_TYPE_ADDON,
    description="Show the migration status of the current workdir",
)
def filestate__migration__status(context: ExecutionContext) -> None:
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

    status = workdir.migration_status()
    current = status["current_version"] or "none"

    context.io.log(f"Current version : {current}")

    if status["applied"]:
        context.io.log(f"Applied         : {', '.join(status['applied'])}")
    else:
        context.io.log("Applied         : (none)")

    if status["pending"]:
        context.io.log(f"Pending         : {', '.join(status['pending'])}")
    else:
        context.io.log("Pending         : (up to date)")
