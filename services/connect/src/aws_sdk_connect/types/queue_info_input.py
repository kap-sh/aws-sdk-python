"""Generated from Smithy shape ``com.amazonaws.connect#QueueInfoInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.queue_id


class QueueInfoInput(TypedDict, closed=True):
    id: NotRequired["aws_sdk_connect.types.queue_id.QueueId"]
    """<p>The identifier of the queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueueInfoInput) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> QueueInfoInput:
    out: QueueInfoInput = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
