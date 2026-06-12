"""Generated from Smithy shape ``com.amazonaws.billingconductor#CustomLineItemType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_billingconductor.errors import DeserializationError

CustomLineItemType: TypeAlias = Literal[
    "CREDIT",
    "FEE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREDIT",
        "FEE",
    )
)


def serialize_json(value: CustomLineItemType) -> str:
    return value


def deserialize_json(data: str) -> CustomLineItemType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomLineItemType value: {data!r}")
    return cast(CustomLineItemType, data)
