"""Generated from Smithy shape ``com.amazonaws.medialive#StopChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class StopChannelRequest(TypedDict, closed=True):
    channel_id: "aws_sdk_medialive.types.__string.__string"
    """A request to stop a running channel"""


# --- restJson1 ser/de ---
def serialize_json(value: StopChannelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopChannelRequest:
    out: StopChannelRequest = {}  # type: ignore[typeddict-item]
    return out
