"""Generated from Smithy shape ``com.amazonaws.rekognition#DatasetLabelDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.dataset_label
    import aws_sdk_rekognition.types.dataset_label_stats


class DatasetLabelDescription(TypedDict, closed=True):
    label_name: NotRequired["aws_sdk_rekognition.types.dataset_label.DatasetLabel"]
    """<p> The name of the label. </p>"""
    label_stats: NotRequired[
        "aws_sdk_rekognition.types.dataset_label_stats.DatasetLabelStats"
    ]
    """<p> Statistics about the label. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetLabelDescription) -> dict:
    out: dict = {}
    if "label_name" in value:
        out["LabelName"] = value["label_name"]
    if "label_stats" in value:
        import aws_sdk_rekognition.types.dataset_label_stats

        out["LabelStats"] = (
            aws_sdk_rekognition.types.dataset_label_stats.serialize_aws_json_1_1(
                value["label_stats"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetLabelDescription:
    out: DatasetLabelDescription = {}  # type: ignore[typeddict-item]
    if "LabelName" in data:
        out["label_name"] = data["LabelName"]
    if "LabelStats" in data:
        import aws_sdk_rekognition.types.dataset_label_stats

        out["label_stats"] = (
            aws_sdk_rekognition.types.dataset_label_stats.deserialize_aws_json_1_1(
                data["LabelStats"]
            )
        )
    return out
