"""Generated from Smithy shape ``com.amazonaws.outposts#QuoteSpecificationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

QuoteSpecificationType: TypeAlias = Literal[
    "UPDATED_RACK",
    "NEW_RACK",
    "EXISTING_RACK",
    "SERVER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UPDATED_RACK",
        "NEW_RACK",
        "EXISTING_RACK",
        "SERVER",
    )
)


def serialize_json(value: QuoteSpecificationType) -> str:
    return value


def deserialize_json(data: str) -> QuoteSpecificationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QuoteSpecificationType value: {data!r}")
    return cast(QuoteSpecificationType, data)
