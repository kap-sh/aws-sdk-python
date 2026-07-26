"""Generated from Smithy shape ``com.amazonaws.deadline#CreateQueueResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.queue_id


class CreateQueueResponse(TypedDict, closed=True):
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """<p>The queue ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQueueResponse) -> dict:
    out: dict = {}
    out["queueId"] = value["queue_id"]
    return out


def deserialize_json(data: dict) -> CreateQueueResponse:
    out: CreateQueueResponse = {}  # type: ignore[typeddict-item]
    if "queueId" in data:
        out["queue_id"] = data["queueId"]
    else:
        raise DeserializationError("CreateQueueResponse.queue_id required")
    return out
