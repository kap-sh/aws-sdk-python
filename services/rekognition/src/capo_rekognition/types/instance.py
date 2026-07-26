"""Generated from Smithy shape ``com.amazonaws.rekognition#Instance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.bounding_box
    import capo_rekognition.types.dominant_colors
    import capo_rekognition.types.percent


class Instance(TypedDict, closed=True):
    bounding_box: NotRequired["capo_rekognition.types.bounding_box.BoundingBox"]
    """<p>The position of the label instance on the image.</p>"""
    confidence: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>The confidence that Amazon Rekognition has in the accuracy of the bounding box.</p>"""
    dominant_colors: NotRequired[
        "capo_rekognition.types.dominant_colors.DominantColors"
    ]
    """<p>The dominant colors found in an individual instance of a label.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Instance) -> dict:
    out: dict = {}
    if "bounding_box" in value:
        import capo_rekognition.types.bounding_box

        out["BoundingBox"] = capo_rekognition.types.bounding_box.serialize_aws_json_1_1(
            value["bounding_box"]
        )
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    if "dominant_colors" in value:
        import capo_rekognition.types.dominant_colors

        out["DominantColors"] = (
            capo_rekognition.types.dominant_colors.serialize_aws_json_1_1(
                value["dominant_colors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Instance:
    out: Instance = {}  # type: ignore[typeddict-item]
    if "BoundingBox" in data:
        import capo_rekognition.types.bounding_box

        out["bounding_box"] = (
            capo_rekognition.types.bounding_box.deserialize_aws_json_1_1(
                data["BoundingBox"]
            )
        )
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    if "DominantColors" in data:
        import capo_rekognition.types.dominant_colors

        out["dominant_colors"] = (
            capo_rekognition.types.dominant_colors.deserialize_aws_json_1_1(
                data["DominantColors"]
            )
        )
    return out
