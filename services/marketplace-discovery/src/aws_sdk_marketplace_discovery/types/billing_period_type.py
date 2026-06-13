"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#BillingPeriodType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_discovery.errors import DeserializationError

BillingPeriodType: TypeAlias = Literal["Monthly",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Monthly",))


def serialize_json(value: BillingPeriodType) -> str:
    return value


def deserialize_json(data: str) -> BillingPeriodType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BillingPeriodType value: {data!r}")
    return cast(BillingPeriodType, data)
