"""Generated from Smithy shape ``com.amazonaws.billingconductor#GroupByAttributeName``."""

from typing import Literal, TypeAlias, cast

GroupByAttributeName: TypeAlias = Literal[
    "PRODUCT_NAME",
    "BILLING_PERIOD",
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupByAttributeName) -> str:
    return value


def deserialize_json(data: str) -> GroupByAttributeName:
    return cast(GroupByAttributeName, data)
