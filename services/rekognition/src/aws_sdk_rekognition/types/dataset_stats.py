"""Generated from Smithy shape ``com.amazonaws.rekognition#DatasetStats``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.u_integer


class DatasetStats(TypedDict):
    labeled_entries: NotRequired["aws_sdk_rekognition.types.u_integer.UInteger"]
    """<p> The total number of images in the dataset that have labels. </p>"""
    total_entries: NotRequired["aws_sdk_rekognition.types.u_integer.UInteger"]
    """<p> The total number of images in the dataset. </p>"""
    total_labels: NotRequired["aws_sdk_rekognition.types.u_integer.UInteger"]
    """<p> The total number of labels declared in the dataset. </p>"""
    error_entries: NotRequired["aws_sdk_rekognition.types.u_integer.UInteger"]
    """<p> The total number of entries that contain at least one error. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetStats) -> dict:
    out: dict = {}
    if "labeled_entries" in value:
        out["LabeledEntries"] = value["labeled_entries"]
    if "total_entries" in value:
        out["TotalEntries"] = value["total_entries"]
    if "total_labels" in value:
        out["TotalLabels"] = value["total_labels"]
    if "error_entries" in value:
        out["ErrorEntries"] = value["error_entries"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetStats:
    out: DatasetStats = {}  # type: ignore[typeddict-item]
    if "LabeledEntries" in data:
        out["labeled_entries"] = data["LabeledEntries"]
    if "TotalEntries" in data:
        out["total_entries"] = data["TotalEntries"]
    if "TotalLabels" in data:
        out["total_labels"] = data["TotalLabels"]
    if "ErrorEntries" in data:
        out["error_entries"] = data["ErrorEntries"]
    return out
