"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectLabelsImageProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.detect_labels_image_background
    import aws_sdk_rekognition.types.detect_labels_image_foreground
    import aws_sdk_rekognition.types.detect_labels_image_quality
    import aws_sdk_rekognition.types.dominant_colors


class DetectLabelsImageProperties(TypedDict):
    quality: NotRequired[
        "aws_sdk_rekognition.types.detect_labels_image_quality.DetectLabelsImageQuality"
    ]
    """<p>Information about the quality of the image foreground as defined by brightness, sharpness, and contrast. The higher the value the greater the brightness, sharpness, and contrast respectively.</p>"""
    dominant_colors: NotRequired[
        "aws_sdk_rekognition.types.dominant_colors.DominantColors"
    ]
    """<p>Information about the dominant colors found in an image, described with RGB values, CSS color name, simplified color name, and PixelPercentage (the percentage of image pixels that have a particular color).</p>"""
    foreground: NotRequired[
        "aws_sdk_rekognition.types.detect_labels_image_foreground.DetectLabelsImageForeground"
    ]
    """<p>Information about the properties of an image’s foreground, including the foreground’s quality and dominant colors, including the quality and dominant colors of the image.</p>"""
    background: NotRequired[
        "aws_sdk_rekognition.types.detect_labels_image_background.DetectLabelsImageBackground"
    ]
    """<p>Information about the properties of an image’s background, including the background’s quality and dominant colors, including the quality and dominant colors of the image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectLabelsImageProperties) -> dict:
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
    if "foreground" in value:
        import aws_sdk_rekognition.types.detect_labels_image_foreground

        out["Foreground"] = (
            aws_sdk_rekognition.types.detect_labels_image_foreground.serialize_aws_json_1_1(
                value["foreground"]
            )
        )
    if "background" in value:
        import aws_sdk_rekognition.types.detect_labels_image_background

        out["Background"] = (
            aws_sdk_rekognition.types.detect_labels_image_background.serialize_aws_json_1_1(
                value["background"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectLabelsImageProperties:
    out: DetectLabelsImageProperties = {}  # type: ignore[typeddict-item]
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
    if "Foreground" in data:
        import aws_sdk_rekognition.types.detect_labels_image_foreground

        out["foreground"] = (
            aws_sdk_rekognition.types.detect_labels_image_foreground.deserialize_aws_json_1_1(
                data["Foreground"]
            )
        )
    if "Background" in data:
        import aws_sdk_rekognition.types.detect_labels_image_background

        out["background"] = (
            aws_sdk_rekognition.types.detect_labels_image_background.deserialize_aws_json_1_1(
                data["Background"]
            )
        )
    return out
