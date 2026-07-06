"""Generated from Smithy shape ``com.amazonaws.mediatailor#SlateSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string


class SlateSource(TypedDict, closed=True):
    source_location_name: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The name of the source location where the slate VOD source is stored.</p>"""
    vod_source_name: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The slate VOD source name. The VOD source must already exist in a source location before it can be used for slate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlateSource) -> dict:
    out: dict = {}
    if "source_location_name" in value:
        out["SourceLocationName"] = value["source_location_name"]
    if "vod_source_name" in value:
        out["VodSourceName"] = value["vod_source_name"]
    return out


def deserialize_json(data: dict) -> SlateSource:
    out: SlateSource = {}  # type: ignore[typeddict-item]
    if "SourceLocationName" in data:
        out["source_location_name"] = data["SourceLocationName"]
    if "VodSourceName" in data:
        out["vod_source_name"] = data["VodSourceName"]
    return out
