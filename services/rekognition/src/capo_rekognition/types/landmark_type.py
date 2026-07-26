"""Generated from Smithy shape ``com.amazonaws.rekognition#LandmarkType``."""

from typing import Literal, TypeAlias, cast

LandmarkType: TypeAlias = Literal[
    "eyeLeft",
    "eyeRight",
    "nose",
    "mouthLeft",
    "mouthRight",
    "leftEyeBrowLeft",
    "leftEyeBrowRight",
    "leftEyeBrowUp",
    "rightEyeBrowLeft",
    "rightEyeBrowRight",
    "rightEyeBrowUp",
    "leftEyeLeft",
    "leftEyeRight",
    "leftEyeUp",
    "leftEyeDown",
    "rightEyeLeft",
    "rightEyeRight",
    "rightEyeUp",
    "rightEyeDown",
    "noseLeft",
    "noseRight",
    "mouthUp",
    "mouthDown",
    "leftPupil",
    "rightPupil",
    "upperJawlineLeft",
    "midJawlineLeft",
    "chinBottom",
    "midJawlineRight",
    "upperJawlineRight",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LandmarkType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LandmarkType:
    return cast(LandmarkType, data)
