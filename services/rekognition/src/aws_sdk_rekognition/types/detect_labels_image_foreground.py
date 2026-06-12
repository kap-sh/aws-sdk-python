"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectLabelsImageForeground``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.detect_labels_image_quality
    import aws_sdk_rekognition.types.dominant_colors


class DetectLabelsImageForeground(TypedDict):
    quality: NotRequired[
        "aws_sdk_rekognition.types.detect_labels_image_quality.DetectLabelsImageQuality"
    ]
    """<p>The quality of the image foreground as defined by brightness and sharpness.</p>"""
    dominant_colors: NotRequired[
        "aws_sdk_rekognition.types.dominant_colors.DominantColors"
    ]
    """<p>The dominant colors found in the foreground of an image, defined with RGB values, CSS color name, simplified color name, and PixelPercentage (the percentage of image pixels that have a particular color).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectLabelsImageForeground) -> dict:
    out: dict = {}
    if "quality" in value:
        import aws_sdk_rekognition.types.detect_labels_image_quality

        out["Quality"] = (
            aws_sdk_rekognition.types.detect_labels_image_quality.serialize_aws_json_1_1(
                value["quality"]
            )
        )
    if "dominant_colors" in value:
        import aws_sdk_rekognition.types.dominant_colors

        out["DominantColors"] = (
            aws_sdk_rekognition.types.dominant_colors.serialize_aws_json_1_1(
                value["dominant_colors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectLabelsImageForeground:
    out: DetectLabelsImageForeground = {}  # type: ignore[typeddict-item]
    if "Quality" in data:
        import aws_sdk_rekognition.types.detect_labels_image_quality

        out["quality"] = (
            aws_sdk_rekognition.types.detect_labels_image_quality.deserialize_aws_json_1_1(
                data["Quality"]
            )
        )
    if "DominantColors" in data:
        import aws_sdk_rekognition.types.dominant_colors

        out["dominant_colors"] = (
            aws_sdk_rekognition.types.dominant_colors.deserialize_aws_json_1_1(
                data["DominantColors"]
            )
        )
    return out
