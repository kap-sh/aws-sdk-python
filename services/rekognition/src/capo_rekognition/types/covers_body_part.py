"""Generated from Smithy shape ``com.amazonaws.rekognition#CoversBodyPart``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.boolean
    import capo_rekognition.types.percent


class CoversBodyPart(TypedDict, closed=True):
    confidence: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>The confidence that Amazon Rekognition has in the value of <code>Value</code>.</p>"""
    value: "capo_rekognition.types.boolean.Boolean"
    """<p>True if the PPE covers the corresponding body part, otherwise false.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CoversBodyPart) -> dict:
    out: dict = {}
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    out["Value"] = value.get("value", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> CoversBodyPart:
    out: CoversBodyPart = {}  # type: ignore[typeddict-item]
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        out["value"] = False
    return out
