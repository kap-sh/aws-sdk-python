"""Generated from Smithy shape ``com.amazonaws.rekognition#LandmarkType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_aws_json_1_1(value: LandmarkType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LandmarkType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LandmarkType value: {data!r}")
    return cast(LandmarkType, data)
