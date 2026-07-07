"""Generated from Smithy shape ``com.amazonaws.iotdataplane#GetRetainedMessageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_data_plane.types.topic


class GetRetainedMessageRequest(TypedDict, closed=True):
    topic: "aws_sdk_iot_data_plane.types.topic.Topic"
    """<p>The topic name of the retained message to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRetainedMessageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRetainedMessageRequest:
    out: GetRetainedMessageRequest = {}  # type: ignore[typeddict-item]
    return out
