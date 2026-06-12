"""Generated from Smithy shape ``com.amazonaws.iot#StopThingRegistrationTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.task_id


class StopThingRegistrationTaskRequest(TypedDict):
    task_id: "aws_sdk_iot.types.task_id.TaskId"
    """<p>The bulk thing provisioning task ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopThingRegistrationTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopThingRegistrationTaskRequest:
    out: StopThingRegistrationTaskRequest = {}  # type: ignore[typeddict-item]
    return out
