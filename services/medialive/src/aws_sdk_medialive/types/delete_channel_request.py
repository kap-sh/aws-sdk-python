"""Generated from Smithy shape ``com.amazonaws.medialive#DeleteChannelRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class DeleteChannelRequest(TypedDict):
    channel_id: "aws_sdk_medialive.types.__string.__string"
    """Unique ID of the channel."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteChannelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteChannelRequest:
    out: DeleteChannelRequest = {}  # type: ignore[typeddict-item]
    return out
