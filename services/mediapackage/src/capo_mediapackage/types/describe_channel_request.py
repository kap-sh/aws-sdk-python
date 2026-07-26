"""Generated from Smithy shape ``com.amazonaws.mediapackage#DescribeChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediapackage.types.__string


class DescribeChannelRequest(TypedDict, closed=True):
    id: "capo_mediapackage.types.__string.__string"
    """The ID of a Channel."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeChannelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeChannelRequest:
    out: DescribeChannelRequest = {}  # type: ignore[typeddict-item]
    return out
