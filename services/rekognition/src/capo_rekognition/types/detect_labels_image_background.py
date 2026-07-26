"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectLabelsImageBackground``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.detect_labels_image_quality
    import capo_rekognition.types.dominant_colors


class DetectLabelsImageBackground(TypedDict, closed=True):
    quality: NotRequired[
        "capo_rekognition.types.detect_labels_image_quality.DetectLabelsImageQuality"
    ]
    """<p>The quality of the image background as defined by brightness and sharpness.</p>"""
    dominant_colors: NotRequired[
        "capo_rekognition.types.dominant_colors.DominantColors"
    ]
    """<p>The dominant colors found in the background of an image, defined with RGB values, CSS color name, simplified color name, and PixelPercentage (the percentage of image pixels that have a particular color).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectLabelsImageBackground) -> dict:
    out: dict = {}
    if "quality" in value:
        import capo_rekognition.types.detect_labels_image_quality

        out["Quality"] = (
            capo_rekognition.types.detect_labels_image_quality.serialize_aws_json_1_1(
                value["quality"]
            )
        )
    if "dominant_colors" in value:
        import capo_rekognition.types.dominant_colors

        out["DominantColors"] = (
            capo_rekognition.types.dominant_colors.serialize_aws_json_1_1(
                value["dominant_colors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectLabelsImageBackground:
    out: DetectLabelsImageBackground = {}  # type: ignore[typeddict-item]
    if "Quality" in data:
        import capo_rekognition.types.detect_labels_image_quality

        out["quality"] = (
            capo_rekognition.types.detect_labels_image_quality.deserialize_aws_json_1_1(
                data["Quality"]
            )
        )
    if "DominantColors" in data:
        import capo_rekognition.types.dominant_colors

        out["dominant_colors"] = (
            capo_rekognition.types.dominant_colors.deserialize_aws_json_1_1(
                data["DominantColors"]
            )
        )
    return out
