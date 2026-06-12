"""Generated from Smithy shape ``com.amazonaws.polly#StreamClosedEvent``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_polly.types.request_characters


class StreamClosedEvent(TypedDict):
    request_characters: "aws_sdk_polly.types.request_characters.RequestCharacters"
    """<p>The total number of characters synthesized during the streaming session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamClosedEvent) -> dict:
    out: dict = {}
    out["RequestCharacters"] = value.get("request_characters", 0)
    return out


def deserialize_json(data: dict) -> StreamClosedEvent:
    out: StreamClosedEvent = {}  # type: ignore[typeddict-item]
    if "RequestCharacters" in data:
        out["request_characters"] = data["RequestCharacters"]
    else:
        out["request_characters"] = 0
    return out
