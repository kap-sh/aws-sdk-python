"""Generated from Smithy shape ``com.amazonaws.connect#StartContactStreamingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.streaming_id


class StartContactStreamingResponse(TypedDict, closed=True):
    streaming_id: "aws_sdk_connect.types.streaming_id.StreamingId"
    """<p>The identifier of the streaming configuration enabled. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartContactStreamingResponse) -> dict:
    out: dict = {}
    out["StreamingId"] = value["streaming_id"]
    return out


def deserialize_json(data: dict) -> StartContactStreamingResponse:
    out: StartContactStreamingResponse = {}  # type: ignore[typeddict-item]
    if "StreamingId" in data:
        out["streaming_id"] = data["StreamingId"]
    else:
        raise DeserializationError(
            "StartContactStreamingResponse.streaming_id required"
        )
    return out
