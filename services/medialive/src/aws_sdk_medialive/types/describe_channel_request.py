"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeChannelRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class DescribeChannelRequest(TypedDict):
    channel_id: "aws_sdk_medialive.types.__string.__string"
    """channel ID"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeChannelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeChannelRequest:
    out: DescribeChannelRequest = {}  # type: ignore[typeddict-item]
    return out
