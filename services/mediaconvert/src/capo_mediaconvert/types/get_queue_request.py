"""Generated from Smithy shape ``com.amazonaws.mediaconvert#GetQueueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string


class GetQueueRequest(TypedDict, closed=True):
    name: "capo_mediaconvert.types.__string.__string"
    """The name of the queue that you want information about."""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueueRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetQueueRequest:
    out: GetQueueRequest = {}  # type: ignore[typeddict-item]
    return out
