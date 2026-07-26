"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#BillingPeriodType``."""

from typing import Literal, TypeAlias, cast

BillingPeriodType: TypeAlias = Literal["Monthly",]


# --- restJson1 ser/de ---
def serialize_json(value: BillingPeriodType) -> str:
    return value


def deserialize_json(data: str) -> BillingPeriodType:
    return cast(BillingPeriodType, data)
