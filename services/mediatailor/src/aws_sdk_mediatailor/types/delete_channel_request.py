"""Generated from Smithy shape ``com.amazonaws.mediatailor#DeleteChannelRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string


class DeleteChannelRequest(TypedDict):
    channel_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteChannelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteChannelRequest:
    out: DeleteChannelRequest = {}  # type: ignore[typeddict-item]
    return out
