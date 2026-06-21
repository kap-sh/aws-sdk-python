"""Generated from Smithy shape ``com.amazonaws.rekognition#Attribute``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: Attribute) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Attribute:
    return cast(Attribute, data)
