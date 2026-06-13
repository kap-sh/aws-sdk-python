"""Generated from Smithy shape ``com.amazonaws.mgn#MergeConstruct``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.construct_id
    import aws_sdk_mgn.types.segment_id


class MergeConstruct(TypedDict):
    segment_id: NotRequired["aws_sdk_mgn.types.segment_id.SegmentID"]
    """<p>The segment ID of the construct to merge.</p>"""
    construct_id: NotRequired["aws_sdk_mgn.types.construct_id.ConstructID"]
    """<p>The construct ID to merge.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MergeConstruct) -> dict:
    out: dict = {}
    if "segment_id" in value:
        out["segmentID"] = value["segment_id"]
    if "construct_id" in value:
        out["constructID"] = value["construct_id"]
    return out


def deserialize_json(data: dict) -> MergeConstruct:
    out: MergeConstruct = {}  # type: ignore[typeddict-item]
    if "segmentID" in data:
        out["segment_id"] = data["segmentID"]
    if "constructID" in data:
        out["construct_id"] = data["constructID"]
    return out
