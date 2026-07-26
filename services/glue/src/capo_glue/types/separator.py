"""Generated from Smithy shape ``com.amazonaws.glue#Separator``."""

from typing import Literal, TypeAlias, cast

Separator: TypeAlias = Literal[
    "comma",
    "ctrla",
    "pipe",
    "semicolon",
    "tab",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Separator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Separator:
    return cast(Separator, data)
