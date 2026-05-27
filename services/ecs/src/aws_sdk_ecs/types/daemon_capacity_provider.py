"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonCapacityProvider``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.integer
    import aws_sdk_ecs.types.string


class DaemonCapacityProvider(TypedDict):
    arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the capacity provider.</p>"""
    running_count: "aws_sdk_ecs.types.integer.Integer"
    """<p>The number of daemon tasks running on this capacity provider.</p>"""
