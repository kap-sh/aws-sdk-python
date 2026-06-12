"""Generated from Smithy shape ``com.amazonaws.outposts#QuotePricingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

QuotePricingType: TypeAlias = Literal["SUBSCRIPTION",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SUBSCRIPTION",))


def serialize_json(value: QuotePricingType) -> str:
    return value


def deserialize_json(data: str) -> QuotePricingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QuotePricingType value: {data!r}")
    return cast(QuotePricingType, data)
