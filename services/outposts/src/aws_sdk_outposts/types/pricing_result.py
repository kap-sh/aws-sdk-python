"""Generated from Smithy shape ``com.amazonaws.outposts#PricingResult``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

PricingResult: TypeAlias = Literal[
    "PRICED",
    "UNABLE_TO_PRICE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRICED",
        "UNABLE_TO_PRICE",
    )
)


def serialize_json(value: PricingResult) -> str:
    return value


def deserialize_json(data: str) -> PricingResult:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PricingResult value: {data!r}")
    return cast(PricingResult, data)
