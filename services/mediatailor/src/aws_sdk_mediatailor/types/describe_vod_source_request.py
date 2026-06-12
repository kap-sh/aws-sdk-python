"""Generated from Smithy shape ``com.amazonaws.mediatailor#DescribeVodSourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string


class DescribeVodSourceRequest(TypedDict):
    source_location_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the source location associated with this VOD Source.</p>"""
    vod_source_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the VOD Source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeVodSourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeVodSourceRequest:
    out: DescribeVodSourceRequest = {}  # type: ignore[typeddict-item]
    return out
