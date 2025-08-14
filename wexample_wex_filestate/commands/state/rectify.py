from typing import TYPE_CHECKING

from wexample_wex_core.decorator.command import command

if TYPE_CHECKING:
    from wexample_wex_core.common.execution_context import ExecutionContext


@command()
def filestate__state__rectify(
        context: "ExecutionContext"
):
    # TODO
    context.io.log('Fixing state...')
