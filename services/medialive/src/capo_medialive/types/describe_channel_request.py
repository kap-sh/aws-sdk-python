"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class DescribeChannelRequest(TypedDict, closed=True):
    channel_id: "capo_medialive.types.__string.__string"
    """channel ID"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeChannelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeChannelRequest:
    out: DescribeChannelRequest = {}  # type: ignore[typeddict-item]
    return out
