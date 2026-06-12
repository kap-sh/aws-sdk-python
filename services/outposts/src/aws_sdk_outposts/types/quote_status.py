"""Generated from Smithy shape ``com.amazonaws.outposts#QuoteStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

QuoteStatus: TypeAlias = Literal[
    "CREATED",
    "ORDER_SUBMITTED",
    "EXPIRED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "ORDER_SUBMITTED",
        "EXPIRED",
    )
)


def serialize_json(value: QuoteStatus) -> str:
    return value


def deserialize_json(data: str) -> QuoteStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QuoteStatus value: {data!r}")
    return cast(QuoteStatus, data)
