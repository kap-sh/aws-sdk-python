"""Generated from Smithy shape ``com.amazonaws.rekognition#Reason``."""

from typing import Literal, TypeAlias, cast

Reason: TypeAlias = Literal[
    "EXCEEDS_MAX_FACES",
    "EXTREME_POSE",
    "LOW_BRIGHTNESS",
    "LOW_SHARPNESS",
    "LOW_CONFIDENCE",
    "SMALL_BOUNDING_BOX",
    "LOW_FACE_QUALITY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Reason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Reason:
    return cast(Reason, data)
