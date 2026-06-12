"""Generated from Smithy shape ``com.amazonaws.glue#QuoteChar``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

QuoteChar: TypeAlias = Literal[
    "quote",
    "quillemet",
    "single_quote",
    "disabled",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "quote",
        "quillemet",
        "single_quote",
        "disabled",
    )
)


def serialize_aws_json_1_1(value: QuoteChar) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QuoteChar:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QuoteChar value: {data!r}")
    return cast(QuoteChar, data)
