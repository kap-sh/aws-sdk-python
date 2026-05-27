"""Generated from Smithy shape ``com.amazonaws.ecs#GetTaskProtectionResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.failures
    import aws_sdk_ecs.types.protected_tasks


class GetTaskProtectionResponse(TypedDict):
    protected_tasks: NotRequired["aws_sdk_ecs.types.protected_tasks.ProtectedTasks"]
    """<p>A list of tasks with the following information.</p> <ul> <li> <p> <code>taskArn</code>: The task ARN.</p> </li> <li> <p> <code>protectionEnabled</code>: The protection status of the task. If scale-in protection is turned on for a task, the value is <code>true</code>. Otherwise, it is <code>false</code>.</p> </li> <li> <p> <code>expirationDate</code>: The epoch time when protection for the task will expire.</p> </li> </ul>"""
    failures: NotRequired["aws_sdk_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p>"""
