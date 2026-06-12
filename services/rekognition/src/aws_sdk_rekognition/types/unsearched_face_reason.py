"""Generated from Smithy shape ``com.amazonaws.rekognition#UnsearchedFaceReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

UnsearchedFaceReason: TypeAlias = Literal[
    "FACE_NOT_LARGEST",
    "EXCEEDS_MAX_FACES",
    "EXTREME_POSE",
    "LOW_BRIGHTNESS",
    "LOW_SHARPNESS",
    "LOW_CONFIDENCE",
    "SMALL_BOUNDING_BOX",
    "LOW_FACE_QUALITY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FACE_NOT_LARGEST",
        "EXCEEDS_MAX_FACES",
        "EXTREME_POSE",
        "LOW_BRIGHTNESS",
        "LOW_SHARPNESS",
        "LOW_CONFIDENCE",
        "SMALL_BOUNDING_BOX",
        "LOW_FACE_QUALITY",
    )
)


def serialize_aws_json_1_1(value: UnsearchedFaceReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UnsearchedFaceReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UnsearchedFaceReason value: {data!r}")
    return cast(UnsearchedFaceReason, data)
