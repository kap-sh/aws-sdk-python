"""Generated from Smithy shape ``com.amazonaws.waf#TextTransformation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_waf.errors import DeserializationError

TextTransformation: TypeAlias = Literal[
    "NONE",
    "COMPRESS_WHITE_SPACE",
    "HTML_ENTITY_DECODE",
    "LOWERCASE",
    "CMD_LINE",
    "URL_DECODE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "COMPRESS_WHITE_SPACE",
        "HTML_ENTITY_DECODE",
        "LOWERCASE",
        "CMD_LINE",
        "URL_DECODE",
    )
)


def serialize_aws_json_1_1(value: TextTransformation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TextTransformation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TextTransformation value: {data!r}")
    return cast(TextTransformation, data)
