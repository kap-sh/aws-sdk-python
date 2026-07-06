"""Generated from Smithy shape ``com.amazonaws.mediapackage#RotateChannelCredentialsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.__string


class RotateChannelCredentialsRequest(TypedDict, closed=True):
    id: "aws_sdk_mediapackage.types.__string.__string"
    """The ID of the channel to update."""


# --- restJson1 ser/de ---
def serialize_json(value: RotateChannelCredentialsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RotateChannelCredentialsRequest:
    out: RotateChannelCredentialsRequest = {}  # type: ignore[typeddict-item]
    return out
