"""Generated from Smithy shape ``com.amazonaws.rekognition#ContentType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.percent
    import aws_sdk_rekognition.types.string


class ContentType(TypedDict):
    confidence: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>The confidence level of the label given</p>"""
    name: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>The name of the label</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContentType) -> dict:
    out: dict = {}
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ContentType:
    out: ContentType = {}  # type: ignore[typeddict-item]
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
