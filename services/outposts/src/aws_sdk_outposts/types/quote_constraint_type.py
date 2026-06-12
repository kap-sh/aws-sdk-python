"""Generated from Smithy shape ``com.amazonaws.outposts#QuoteConstraintType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

QuoteConstraintType: TypeAlias = Literal[
    "RACK_MAXIMUM",
    "RACK_MAX_POWER_KVA",
    "RACK_MAX_WEIGHT_LBS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RACK_MAXIMUM",
        "RACK_MAX_POWER_KVA",
        "RACK_MAX_WEIGHT_LBS",
    )
)


def serialize_json(value: QuoteConstraintType) -> str:
    return value


def deserialize_json(data: str) -> QuoteConstraintType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QuoteConstraintType value: {data!r}")
    return cast(QuoteConstraintType, data)
