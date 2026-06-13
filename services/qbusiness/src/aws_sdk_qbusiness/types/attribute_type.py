"""Generated from Smithy shape ``com.amazonaws.qbusiness#AttributeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

AttributeType: TypeAlias = Literal[
    "STRING",
    "STRING_LIST",
    "NUMBER",
    "DATE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STRING",
        "STRING_LIST",
        "NUMBER",
        "DATE",
    )
)


def serialize_json(value: AttributeType) -> str:
    return value


def deserialize_json(data: str) -> AttributeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AttributeType value: {data!r}")
    return cast(AttributeType, data)
