"""Generated from Smithy shape ``com.amazonaws.pinpoint#SegmentReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__integer
    import aws_sdk_pinpoint.types.__string


class SegmentReference(TypedDict, closed=True):
    id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the segment.</p>"""
    version: NotRequired["aws_sdk_pinpoint.types.__integer.__integer"]
    """<p>The version number of the segment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SegmentReference) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> SegmentReference:
    out: SegmentReference = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Version" in data:
        out["version"] = data["Version"]
    return out
