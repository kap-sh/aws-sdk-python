"""Generated from Smithy shape ``com.amazonaws.rekognition#DatasetLabelStats``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.u_integer


class DatasetLabelStats(TypedDict, closed=True):
    entry_count: NotRequired["capo_rekognition.types.u_integer.UInteger"]
    """<p> The total number of images that use the label. </p>"""
    bounding_box_count: NotRequired["capo_rekognition.types.u_integer.UInteger"]
    """<p> The total number of images that have the label assigned to a bounding box. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetLabelStats) -> dict:
    out: dict = {}
    if "entry_count" in value:
        out["EntryCount"] = value["entry_count"]
    if "bounding_box_count" in value:
        out["BoundingBoxCount"] = value["bounding_box_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetLabelStats:
    out: DatasetLabelStats = {}  # type: ignore[typeddict-item]
    if "EntryCount" in data:
        out["entry_count"] = data["EntryCount"]
    if "BoundingBoxCount" in data:
        out["bounding_box_count"] = data["BoundingBoxCount"]
    return out
