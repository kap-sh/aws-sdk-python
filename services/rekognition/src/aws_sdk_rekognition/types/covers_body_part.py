"""Generated from Smithy shape ``com.amazonaws.rekognition#CoversBodyPart``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.boolean
    import aws_sdk_rekognition.types.percent


class CoversBodyPart(TypedDict):
    confidence: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>The confidence that Amazon Rekognition has in the value of <code>Value</code>.</p>"""
    value: "aws_sdk_rekognition.types.boolean.Boolean"
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
