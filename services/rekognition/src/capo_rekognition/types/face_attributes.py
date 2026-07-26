"""Generated from Smithy shape ``com.amazonaws.rekognition#FaceAttributes``."""

from typing import Literal, TypeAlias, cast

FaceAttributes: TypeAlias = Literal[
    "DEFAULT",
    "ALL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FaceAttributes) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FaceAttributes:
    return cast(FaceAttributes, data)
