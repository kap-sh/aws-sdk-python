"""Generated from Smithy shape ``com.amazonaws.iot#StartThingRegistrationTaskResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.task_id


class StartThingRegistrationTaskResponse(TypedDict):
    task_id: NotRequired["aws_sdk_iot.types.task_id.TaskId"]
    """<p>The bulk thing provisioning task ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartThingRegistrationTaskResponse) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    return out


def deserialize_json(data: dict) -> StartThingRegistrationTaskResponse:
    out: StartThingRegistrationTaskResponse = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    return out
