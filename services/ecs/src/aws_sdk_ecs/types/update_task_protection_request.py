"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateTaskProtectionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boolean
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list


class UpdateTaskProtectionRequest(TypedDict):
    cluster: "aws_sdk_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task sets exist in.</p>"""
    tasks: "aws_sdk_ecs.types.string_list.StringList"
    """<p>A list of up to 10 task IDs or full ARN entries.</p>"""
    protection_enabled: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>Specify <code>true</code> to mark a task for protection and <code>false</code> to unset protection, making it eligible for termination.</p>"""
    expires_in_minutes: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>If you set <code>protectionEnabled</code> to <code>true</code>, you can specify the duration for task protection in minutes. You can specify a value from 1 minute to up to 2,880 minutes (48 hours). During this time, your task will not be terminated by scale-in events from Service Auto Scaling or deployments. After this time period lapses, <code>protectionEnabled</code> will be reset to <code>false</code>.</p> <p>If you don’t specify the time, then the task is automatically protected for 120 minutes (2 hours).</p>"""
