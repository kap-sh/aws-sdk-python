"""Generated from Smithy shape ``com.amazonaws.glue#Separator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

Separator: TypeAlias = Literal[
    "comma",
    "ctrla",
    "pipe",
    "semicolon",
    "tab",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "comma",
        "ctrla",
        "pipe",
        "semicolon",
        "tab",
    )
)


def serialize_aws_json_1_1(value: Separator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Separator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Separator value: {data!r}")
    return cast(Separator, data)
