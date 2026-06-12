"""Generated from Smithy shape ``com.amazonaws.billingconductor#GroupByAttributeName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_billingconductor.errors import DeserializationError

GroupByAttributeName: TypeAlias = Literal[
    "PRODUCT_NAME",
    "BILLING_PERIOD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRODUCT_NAME",
        "BILLING_PERIOD",
    )
)


def serialize_json(value: GroupByAttributeName) -> str:
    return value


def deserialize_json(data: str) -> GroupByAttributeName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GroupByAttributeName value: {data!r}")
    return cast(GroupByAttributeName, data)
