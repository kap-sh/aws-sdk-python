"""Generated from Smithy shape ``com.amazonaws.pi#TextFormat``."""

from typing import Literal, TypeAlias, cast

TextFormat: TypeAlias = Literal[
    "PLAIN_TEXT",
    "MARKDOWN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TextFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TextFormat:
    return cast(TextFormat, data)
