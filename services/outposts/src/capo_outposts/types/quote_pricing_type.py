"""Generated from Smithy shape ``com.amazonaws.outposts#QuotePricingType``."""

from typing import Literal, TypeAlias, cast

QuotePricingType: TypeAlias = Literal["SUBSCRIPTION",]


# --- restJson1 ser/de ---
def serialize_json(value: QuotePricingType) -> str:
    return value


def deserialize_json(data: str) -> QuotePricingType:
    return cast(QuotePricingType, data)
