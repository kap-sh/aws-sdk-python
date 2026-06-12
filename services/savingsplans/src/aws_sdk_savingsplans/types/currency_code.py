"""Generated from Smithy shape ``com.amazonaws.savingsplans#CurrencyCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_savingsplans.errors import DeserializationError

CurrencyCode: TypeAlias = Literal[
    "CNY",
    "USD",
    "EUR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CNY",
        "USD",
        "EUR",
    )
)


def serialize_json(value: CurrencyCode) -> str:
    return value


def deserialize_json(data: str) -> CurrencyCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CurrencyCode value: {data!r}")
    return cast(CurrencyCode, data)
