"""Generated from Smithy shape ``com.amazonaws.rekognition#Pose``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.degree


class Pose(TypedDict):
    roll: NotRequired["aws_sdk_rekognition.types.degree.Degree"]
    """<p>Value representing the face rotation on the roll axis.</p>"""
    yaw: NotRequired["aws_sdk_rekognition.types.degree.Degree"]
    """<p>Value representing the face rotation on the yaw axis.</p>"""
    pitch: NotRequired["aws_sdk_rekognition.types.degree.Degree"]
    """<p>Value representing the face rotation on the pitch axis.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Pose) -> dict:
    out: dict = {}
    if "roll" in value:
        out["Roll"] = value["roll"]
    if "yaw" in value:
        out["Yaw"] = value["yaw"]
    if "pitch" in value:
        out["Pitch"] = value["pitch"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Pose:
    out: Pose = {}  # type: ignore[typeddict-item]
    if "Roll" in data:
        out["roll"] = data["Roll"]
    if "Yaw" in data:
        out["yaw"] = data["Yaw"]
    if "Pitch" in data:
        out["pitch"] = data["Pitch"]
    return out
