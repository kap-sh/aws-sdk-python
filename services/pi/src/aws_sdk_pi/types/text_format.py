"""Generated from Smithy shape ``com.amazonaws.pi#TextFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pi.errors import DeserializationError

TextFormat: TypeAlias = Literal[
    "PLAIN_TEXT",
    "MARKDOWN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PLAIN_TEXT",
        "MARKDOWN",
    )
)


def serialize_aws_json_1_1(value: TextFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TextFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TextFormat value: {data!r}")
    return cast(TextFormat, data)
