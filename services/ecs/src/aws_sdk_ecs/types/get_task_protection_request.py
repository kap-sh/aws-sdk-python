"""Generated from Smithy shape ``com.amazonaws.ecs#GetTaskProtectionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list


class GetTaskProtectionRequest(TypedDict):
    cluster: "aws_sdk_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task sets exist in.</p>"""
    tasks: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>A list of up to 100 task IDs or full ARN entries.</p>"""
