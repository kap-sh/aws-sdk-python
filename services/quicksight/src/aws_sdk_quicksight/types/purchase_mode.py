"""Generated from Smithy shape ``com.amazonaws.quicksight#PurchaseMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

PurchaseMode: TypeAlias = Literal[
    "MANUAL",
    "AUTO_PURCHASE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MANUAL",
        "AUTO_PURCHASE",
    )
)


def serialize_json(value: PurchaseMode) -> str:
    return value


def deserialize_json(data: str) -> PurchaseMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PurchaseMode value: {data!r}")
    return cast(PurchaseMode, data)
