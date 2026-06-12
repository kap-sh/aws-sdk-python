"""Generated from Smithy shape ``com.amazonaws.connect#ContactSearchSummaryQueueInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.queue_id
    import aws_sdk_connect.types.timestamp


class ContactSearchSummaryQueueInfo(TypedDict):
    id: NotRequired["aws_sdk_connect.types.queue_id.QueueId"]
    """<p>The unique identifier for the queue.</p>"""
    enqueue_timestamp: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the contact was added to the queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactSearchSummaryQueueInfo) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "enqueue_timestamp" in value:
        import aws_sdk_connect.types.timestamp

        out["EnqueueTimestamp"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["enqueue_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> ContactSearchSummaryQueueInfo:
    out: ContactSearchSummaryQueueInfo = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "EnqueueTimestamp" in data:
        import aws_sdk_connect.types.timestamp

        out["enqueue_timestamp"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["EnqueueTimestamp"]
        )
    return out
