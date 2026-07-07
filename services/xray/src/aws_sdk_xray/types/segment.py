"""Generated from Smithy shape ``com.amazonaws.xray#Segment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_xray.types.segment_document
    import aws_sdk_xray.types.segment_id


class Segment(TypedDict, closed=True):
    id: NotRequired["aws_sdk_xray.types.segment_id.SegmentId"]
    """<p>The segment's ID.</p>"""
    document: NotRequired["aws_sdk_xray.types.segment_document.SegmentDocument"]
    """<p>The segment document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Segment) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "document" in value:
        out["Document"] = value["document"]
    return out


def deserialize_json(data: dict) -> Segment:
    out: Segment = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Document" in data:
        out["document"] = data["Document"]
    return out
