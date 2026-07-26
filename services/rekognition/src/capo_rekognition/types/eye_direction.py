"""Generated from Smithy shape ``com.amazonaws.rekognition#EyeDirection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.degree
    import capo_rekognition.types.percent


class EyeDirection(TypedDict, closed=True):
    yaw: NotRequired["capo_rekognition.types.degree.Degree"]
    """<p>Value representing eye direction on the yaw axis.</p>"""
    pitch: NotRequired["capo_rekognition.types.degree.Degree"]
    """<p>Value representing eye direction on the pitch axis.</p>"""
    confidence: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>The confidence that the service has in its predicted eye direction.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EyeDirection) -> dict:
    out: dict = {}
    if "yaw" in value:
        out["Yaw"] = value["yaw"]
    if "pitch" in value:
        out["Pitch"] = value["pitch"]
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EyeDirection:
    out: EyeDirection = {}  # type: ignore[typeddict-item]
    if "Yaw" in data:
        out["yaw"] = data["Yaw"]
    if "Pitch" in data:
        out["pitch"] = data["Pitch"]
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    return out
