"""Generated from Smithy shape ``com.amazonaws.rekognition#FaceOccluded``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.boolean
    import aws_sdk_rekognition.types.percent


class FaceOccluded(TypedDict):
    value: "aws_sdk_rekognition.types.boolean.Boolean"
    """<p>True if a detected face’s eyes, nose, and mouth are partially captured or if they are covered by masks, dark sunglasses, cell phones, hands, or other objects. False if common occurrences that do not impact face verification are detected, such as eye glasses, lightly tinted sunglasses, strands of hair, and others.</p>"""
    confidence: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>The confidence that the service has detected the presence of a face occlusion.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FaceOccluded) -> dict:
    out: dict = {}
    out["Value"] = value.get("value", False)
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FaceOccluded:
    out: FaceOccluded = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        out["value"] = False
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    return out
