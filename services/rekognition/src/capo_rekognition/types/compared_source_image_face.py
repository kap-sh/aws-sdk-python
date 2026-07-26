"""Generated from Smithy shape ``com.amazonaws.rekognition#ComparedSourceImageFace``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.bounding_box
    import capo_rekognition.types.percent


class ComparedSourceImageFace(TypedDict, closed=True):
    bounding_box: NotRequired["capo_rekognition.types.bounding_box.BoundingBox"]
    """<p>Bounding box of the face.</p>"""
    confidence: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>Confidence level that the selected bounding box contains a face.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComparedSourceImageFace) -> dict:
    out: dict = {}
    if "bounding_box" in value:
        import capo_rekognition.types.bounding_box

        out["BoundingBox"] = capo_rekognition.types.bounding_box.serialize_aws_json_1_1(
            value["bounding_box"]
        )
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ComparedSourceImageFace:
    out: ComparedSourceImageFace = {}  # type: ignore[typeddict-item]
    if "BoundingBox" in data:
        import capo_rekognition.types.bounding_box

        out["bounding_box"] = (
            capo_rekognition.types.bounding_box.deserialize_aws_json_1_1(
                data["BoundingBox"]
            )
        )
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    return out
