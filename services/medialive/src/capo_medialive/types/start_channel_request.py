"""Generated from Smithy shape ``com.amazonaws.medialive#StartChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class StartChannelRequest(TypedDict, closed=True):
    channel_id: "capo_medialive.types.__string.__string"
    """A request to start a channel"""


# --- restJson1 ser/de ---
def serialize_json(value: StartChannelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartChannelRequest:
    out: StartChannelRequest = {}  # type: ignore[typeddict-item]
    return out
