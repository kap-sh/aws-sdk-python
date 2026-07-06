"""Generated from Smithy shape ``com.amazonaws.ecs#StopTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.task


class StopTaskResponse(TypedDict, closed=True):
    task: NotRequired["aws_sdk_ecs.types.task.Task"]
    """<p>The task that was stopped.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopTaskResponse) -> dict:
    out: dict = {}
    if "task" in value:
        import aws_sdk_ecs.types.task

        out["task"] = aws_sdk_ecs.types.task.serialize_aws_json_1_1(value["task"])
    return out


def deserialize_aws_json_1_1(data: dict) -> StopTaskResponse:
    out: StopTaskResponse = {}  # type: ignore[typeddict-item]
    if "task" in data:
        import aws_sdk_ecs.types.task

        out["task"] = aws_sdk_ecs.types.task.deserialize_aws_json_1_1(data["task"])
    return out
