"""Generated from Smithy shape ``com.amazonaws.deadline#CreateQueueEnvironmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.queue_environment_id


class CreateQueueEnvironmentResponse(TypedDict, closed=True):
    queue_environment_id: (
        "aws_sdk_deadline.types.queue_environment_id.QueueEnvironmentId"
    )
    """<p>The queue environment ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQueueEnvironmentResponse) -> dict:
    out: dict = {}
    out["queueEnvironmentId"] = value["queue_environment_id"]
    return out


def deserialize_json(data: dict) -> CreateQueueEnvironmentResponse:
    out: CreateQueueEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if "queueEnvironmentId" in data:
        out["queue_environment_id"] = data["queueEnvironmentId"]
    else:
        raise DeserializationError(
            "CreateQueueEnvironmentResponse.queue_environment_id required"
        )
    return out
