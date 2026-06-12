"""Generated from Smithy shape ``com.amazonaws.wafv2#TextTransformationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

TextTransformationType: TypeAlias = Literal[
    "NONE",
    "COMPRESS_WHITE_SPACE",
    "HTML_ENTITY_DECODE",
    "LOWERCASE",
    "CMD_LINE",
    "URL_DECODE",
    "BASE64_DECODE",
    "HEX_DECODE",
    "MD5",
    "REPLACE_COMMENTS",
    "ESCAPE_SEQ_DECODE",
    "SQL_HEX_DECODE",
    "CSS_DECODE",
    "JS_DECODE",
    "NORMALIZE_PATH",
    "NORMALIZE_PATH_WIN",
    "REMOVE_NULLS",
    "REPLACE_NULLS",
    "BASE64_DECODE_EXT",
    "URL_DECODE_UNI",
    "UTF8_TO_UNICODE",
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
        "BASE64_DECODE",
        "HEX_DECODE",
        "MD5",
        "REPLACE_COMMENTS",
        "ESCAPE_SEQ_DECODE",
        "SQL_HEX_DECODE",
        "CSS_DECODE",
        "JS_DECODE",
        "NORMALIZE_PATH",
        "NORMALIZE_PATH_WIN",
        "REMOVE_NULLS",
        "REPLACE_NULLS",
        "BASE64_DECODE_EXT",
        "URL_DECODE_UNI",
        "UTF8_TO_UNICODE",
    )
)


def serialize_aws_json_1_1(value: TextTransformationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TextTransformationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TextTransformationType value: {data!r}")
    return cast(TextTransformationType, data)
