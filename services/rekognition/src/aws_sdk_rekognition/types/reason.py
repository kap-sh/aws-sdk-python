"""Generated from Smithy shape ``com.amazonaws.rekognition#Reason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "EXCEEDS_MAX_FACES",
        "EXTREME_POSE",
        "LOW_BRIGHTNESS",
        "LOW_SHARPNESS",
        "LOW_CONFIDENCE",
        "SMALL_BOUNDING_BOX",
        "LOW_FACE_QUALITY",
    )
)


def serialize_aws_json_1_1(value: Reason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Reason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Reason value: {data!r}")
    return cast(Reason, data)
