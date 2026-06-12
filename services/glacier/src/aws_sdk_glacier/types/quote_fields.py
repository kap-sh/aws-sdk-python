"""Generated from Smithy shape ``com.amazonaws.glacier#QuoteFields``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glacier.errors import DeserializationError

QuoteFields: TypeAlias = Literal[
    "ALWAYS",
    "ASNEEDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALWAYS",
        "ASNEEDED",
    )
)


def serialize_json(value: QuoteFields) -> str:
    return value


def deserialize_json(data: str) -> QuoteFields:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QuoteFields value: {data!r}")
    return cast(QuoteFields, data)
