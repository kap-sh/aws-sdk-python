"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectCustomLabelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.custom_labels


class DetectCustomLabelsResponse(TypedDict, closed=True):
    custom_labels: NotRequired["aws_sdk_rekognition.types.custom_labels.CustomLabels"]
    """<p>An array of custom labels detected in the input image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectCustomLabelsResponse) -> dict:
    out: dict = {}
    if "custom_labels" in value:
        import aws_sdk_rekognition.types.custom_labels

        out["CustomLabels"] = (
            aws_sdk_rekognition.types.custom_labels.serialize_aws_json_1_1(
                value["custom_labels"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectCustomLabelsResponse:
    out: DetectCustomLabelsResponse = {}  # type: ignore[typeddict-item]
    if "CustomLabels" in data:
        import aws_sdk_rekognition.types.custom_labels

        out["custom_labels"] = (
            aws_sdk_rekognition.types.custom_labels.deserialize_aws_json_1_1(
                data["CustomLabels"]
            )
        )
    return out
