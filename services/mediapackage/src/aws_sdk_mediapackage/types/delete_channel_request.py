"""Generated from Smithy shape ``com.amazonaws.mediapackage#DeleteChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.__string


class DeleteChannelRequest(TypedDict, closed=True):
    id: "aws_sdk_mediapackage.types.__string.__string"
    """The ID of the Channel to delete."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteChannelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteChannelRequest:
    out: DeleteChannelRequest = {}  # type: ignore[typeddict-item]
    return out
