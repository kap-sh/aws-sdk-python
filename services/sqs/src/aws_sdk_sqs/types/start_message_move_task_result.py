"""Generated from Smithy shape ``com.amazonaws.sqs#StartMessageMoveTaskResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sqs.types.string


class StartMessageMoveTaskResult(TypedDict, closed=True):
    task_handle: NotRequired["aws_sdk_sqs.types.string.String"]
    """<p>An identifier associated with a message movement task. You can use this identifier to cancel a specified message movement task using the <code>CancelMessageMoveTask</code> action.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartMessageMoveTaskResult) -> dict:
    out: dict = {}
    if "task_handle" in value:
        out["TaskHandle"] = value["task_handle"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartMessageMoveTaskResult:
    out: StartMessageMoveTaskResult = {}  # type: ignore[typeddict-item]
    if "TaskHandle" in data:
        out["task_handle"] = data["TaskHandle"]
    return out
