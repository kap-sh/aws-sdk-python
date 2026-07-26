"""Generated from Smithy shape ``com.amazonaws.rekognition#GenderType``."""

from typing import Literal, TypeAlias, cast

GenderType: TypeAlias = Literal[
    "Male",
    "Female",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GenderType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GenderType:
    return cast(GenderType, data)
