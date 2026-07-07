"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectLabelsImagePropertiesSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.detect_labels_max_dominant_colors


class DetectLabelsImagePropertiesSettings(TypedDict, closed=True):
    max_dominant_colors: "aws_sdk_rekognition.types.detect_labels_max_dominant_colors.DetectLabelsMaxDominantColors"
    """<p>The maximum number of dominant colors to return when detecting labels in an image. The default value is 10.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectLabelsImagePropertiesSettings) -> dict:
    out: dict = {}
    out["MaxDominantColors"] = value.get("max_dominant_colors", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectLabelsImagePropertiesSettings:
    out: DetectLabelsImagePropertiesSettings = {}  # type: ignore[typeddict-item]
    if "MaxDominantColors" in data:
        out["max_dominant_colors"] = data["MaxDominantColors"]
    else:
        out["max_dominant_colors"] = 0
    return out
