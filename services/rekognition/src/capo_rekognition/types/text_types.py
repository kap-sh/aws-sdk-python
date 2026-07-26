"""Generated from Smithy shape ``com.amazonaws.rekognition#TextTypes``."""

from typing import Literal, TypeAlias, cast

TextTypes: TypeAlias = Literal[
    "LINE",
    "WORD",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TextTypes) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TextTypes:
    return cast(TextTypes, data)
