"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectLabelsSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.detect_labels_image_properties_settings
    import capo_rekognition.types.general_labels_settings


class DetectLabelsSettings(TypedDict, closed=True):
    general_labels: NotRequired[
        "capo_rekognition.types.general_labels_settings.GeneralLabelsSettings"
    ]
    """<p>Contains the specified filters for GENERAL_LABELS.</p>"""
    image_properties: NotRequired[
        "capo_rekognition.types.detect_labels_image_properties_settings.DetectLabelsImagePropertiesSettings"
    ]
    """<p>Contains the chosen number of maximum dominant colors in an image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectLabelsSettings) -> dict:
    out: dict = {}
    if "general_labels" in value:
        import capo_rekognition.types.general_labels_settings

        out["GeneralLabels"] = (
            capo_rekognition.types.general_labels_settings.serialize_aws_json_1_1(
                value["general_labels"]
            )
        )
    if "image_properties" in value:
        import capo_rekognition.types.detect_labels_image_properties_settings

        out["ImageProperties"] = (
            capo_rekognition.types.detect_labels_image_properties_settings.serialize_aws_json_1_1(
                value["image_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectLabelsSettings:
    out: DetectLabelsSettings = {}  # type: ignore[typeddict-item]
    if "GeneralLabels" in data:
        import capo_rekognition.types.general_labels_settings

        out["general_labels"] = (
            capo_rekognition.types.general_labels_settings.deserialize_aws_json_1_1(
                data["GeneralLabels"]
            )
        )
    if "ImageProperties" in data:
        import capo_rekognition.types.detect_labels_image_properties_settings

        out["image_properties"] = (
            capo_rekognition.types.detect_labels_image_properties_settings.deserialize_aws_json_1_1(
                data["ImageProperties"]
            )
        )
    return out
