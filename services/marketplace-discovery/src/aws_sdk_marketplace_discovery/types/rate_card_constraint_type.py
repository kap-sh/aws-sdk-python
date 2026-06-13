"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#RateCardConstraintType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_discovery.errors import DeserializationError

RateCardConstraintType: TypeAlias = Literal[
    "Allowed",
    "Disallowed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Allowed",
        "Disallowed",
    )
)


def serialize_json(value: RateCardConstraintType) -> str:
    return value


def deserialize_json(data: str) -> RateCardConstraintType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RateCardConstraintType value: {data!r}")
    return cast(RateCardConstraintType, data)
