"""Generated from Smithy shape ``com.amazonaws.textract#TextType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_textract.errors import DeserializationError

TextType: TypeAlias = Literal[
    "HANDWRITING",
    "PRINTED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HANDWRITING",
        "PRINTED",
    )
)


def serialize_aws_json_1_1(value: TextType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TextType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TextType value: {data!r}")
    return cast(TextType, data)
