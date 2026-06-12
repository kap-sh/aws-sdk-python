"""Generated from Smithy shape ``com.amazonaws.billingconductor#CurrencyCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_billingconductor.errors import DeserializationError

CurrencyCode: TypeAlias = Literal[
    "USD",
    "CNY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USD",
        "CNY",
    )
)


def serialize_json(value: CurrencyCode) -> str:
    return value


def deserialize_json(data: str) -> CurrencyCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CurrencyCode value: {data!r}")
    return cast(CurrencyCode, data)
