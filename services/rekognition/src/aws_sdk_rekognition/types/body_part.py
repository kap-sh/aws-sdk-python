"""Generated from Smithy shape ``com.amazonaws.rekognition#BodyPart``."""

from typing import Literal, TypeAlias, cast

BodyPart: TypeAlias = Literal[
    "FACE",
    "HEAD",
    "LEFT_HAND",
    "RIGHT_HAND",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BodyPart) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BodyPart:
    return cast(BodyPart, data)
