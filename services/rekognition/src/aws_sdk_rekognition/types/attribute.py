"""Generated from Smithy shape ``com.amazonaws.rekognition#Attribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

Attribute: TypeAlias = Literal[
    "DEFAULT",
    "ALL",
    "AGE_RANGE",
    "BEARD",
    "EMOTIONS",
    "EYE_DIRECTION",
    "EYEGLASSES",
    "EYES_OPEN",
    "GENDER",
    "MOUTH_OPEN",
    "MUSTACHE",
    "FACE_OCCLUDED",
    "SMILE",
    "SUNGLASSES",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "ALL",
        "AGE_RANGE",
        "BEARD",
        "EMOTIONS",
        "EYE_DIRECTION",
        "EYEGLASSES",
        "EYES_OPEN",
        "GENDER",
        "MOUTH_OPEN",
        "MUSTACHE",
        "FACE_OCCLUDED",
        "SMILE",
        "SUNGLASSES",
    )
)


def serialize_aws_json_1_1(value: Attribute) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Attribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Attribute value: {data!r}")
    return cast(Attribute, data)
