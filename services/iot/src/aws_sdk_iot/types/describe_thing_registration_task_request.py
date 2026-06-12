"""Generated from Smithy shape ``com.amazonaws.iot#DescribeThingRegistrationTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.task_id


class DescribeThingRegistrationTaskRequest(TypedDict):
    task_id: "aws_sdk_iot.types.task_id.TaskId"
    """<p>The task ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeThingRegistrationTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeThingRegistrationTaskRequest:
    out: DescribeThingRegistrationTaskRequest = {}  # type: ignore[typeddict-item]
    return out
