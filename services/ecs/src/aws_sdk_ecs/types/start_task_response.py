"""Generated from Smithy shape ``com.amazonaws.ecs#StartTaskResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.failures
    import aws_sdk_ecs.types.tasks


class StartTaskResponse(TypedDict):
    tasks: NotRequired["aws_sdk_ecs.types.tasks.Tasks"]
    """<p>A full description of the tasks that were started. Each task that was successfully placed on your container instances is described.</p>"""
    failures: NotRequired["aws_sdk_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p>"""
