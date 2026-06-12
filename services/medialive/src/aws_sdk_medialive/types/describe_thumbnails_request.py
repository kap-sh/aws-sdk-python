"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeThumbnailsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class DescribeThumbnailsRequest(TypedDict):
    channel_id: "aws_sdk_medialive.types.__string.__string"
    """Unique ID of the channel"""
    pipeline_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Pipeline ID (\"0\" or \"1\")"""
    thumbnail_type: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """thumbnail type"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeThumbnailsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeThumbnailsRequest:
    out: DescribeThumbnailsRequest = {}  # type: ignore[typeddict-item]
    return out
