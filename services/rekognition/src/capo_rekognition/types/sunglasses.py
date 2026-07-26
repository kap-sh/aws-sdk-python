"""Generated from Smithy shape ``com.amazonaws.rekognition#Sunglasses``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.boolean
    import capo_rekognition.types.percent


class Sunglasses(TypedDict, closed=True):
    value: "capo_rekognition.types.boolean.Boolean"
    """<p>Boolean value that indicates whether the face is wearing sunglasses or not.</p>"""
    confidence: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>Level of confidence in the determination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Sunglasses) -> dict:
    out: dict = {}
    out["Value"] = value.get("value", False)
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Sunglasses:
    out: Sunglasses = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        out["value"] = False
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    return out
