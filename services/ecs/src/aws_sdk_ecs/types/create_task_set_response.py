"""Generated from Smithy shape ``com.amazonaws.ecs#CreateTaskSetResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.task_set


class CreateTaskSetResponse(TypedDict):
    task_set: NotRequired["aws_sdk_ecs.types.task_set.TaskSet"]
    """<p>Information about a set of Amazon ECS tasks in either an CodeDeploy or an <code>EXTERNAL</code> deployment. A task set includes details such as the desired number of tasks, how many tasks are running, and whether the task set serves production traffic.</p>"""
