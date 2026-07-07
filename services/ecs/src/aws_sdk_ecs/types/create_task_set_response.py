"""Generated from Smithy shape ``com.amazonaws.ecs#CreateTaskSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.task_set


class CreateTaskSetResponse(TypedDict, closed=True):
    task_set: NotRequired["aws_sdk_ecs.types.task_set.TaskSet"]
    """<p>Information about a set of Amazon ECS tasks in either an CodeDeploy or an <code>EXTERNAL</code> deployment. A task set includes details such as the desired number of tasks, how many tasks are running, and whether the task set serves production traffic.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTaskSetResponse) -> dict:
    out: dict = {}
    if "task_set" in value:
        import aws_sdk_ecs.types.task_set

        out["taskSet"] = aws_sdk_ecs.types.task_set.serialize_aws_json_1_1(
            value["task_set"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTaskSetResponse:
    out: CreateTaskSetResponse = {}  # type: ignore[typeddict-item]
    if "taskSet" in data:
        import aws_sdk_ecs.types.task_set

        out["task_set"] = aws_sdk_ecs.types.task_set.deserialize_aws_json_1_1(
            data["taskSet"]
        )
    return out
