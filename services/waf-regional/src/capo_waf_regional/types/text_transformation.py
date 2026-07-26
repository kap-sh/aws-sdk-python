"""Generated from Smithy shape ``com.amazonaws.wafregional#TextTransformation``."""

from typing import Literal, TypeAlias, cast

TextTransformation: TypeAlias = Literal[
    "NONE",
    "COMPRESS_WHITE_SPACE",
    "HTML_ENTITY_DECODE",
    "LOWERCASE",
    "CMD_LINE",
    "URL_DECODE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TextTransformation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TextTransformation:
    return cast(TextTransformation, data)
