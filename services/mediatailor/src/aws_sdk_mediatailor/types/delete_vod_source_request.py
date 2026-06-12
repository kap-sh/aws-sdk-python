"""Generated from Smithy shape ``com.amazonaws.mediatailor#DeleteVodSourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string


class DeleteVodSourceRequest(TypedDict):
    source_location_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the source location associated with this VOD Source.</p>"""
    vod_source_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the VOD source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVodSourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteVodSourceRequest:
    out: DeleteVodSourceRequest = {}  # type: ignore[typeddict-item]
    return out
