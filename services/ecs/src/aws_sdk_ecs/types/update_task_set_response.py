"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateTaskSetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.task_set


class UpdateTaskSetResponse(TypedDict):
    task_set: NotRequired["aws_sdk_ecs.types.task_set.TaskSet"]
    """<p>Details about the task set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTaskSetResponse) -> dict:
    out: dict = {}
    if "task_set" in value:
        import aws_sdk_ecs.types.task_set

        out["taskSet"] = aws_sdk_ecs.types.task_set.serialize_aws_json_1_1(
            value["task_set"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTaskSetResponse:
    out: UpdateTaskSetResponse = {}  # type: ignore[typeddict-item]
    if "taskSet" in data:
        import aws_sdk_ecs.types.task_set

        out["task_set"] = aws_sdk_ecs.types.task_set.deserialize_aws_json_1_1(
            data["taskSet"]
        )
    return out
