"""Generated from Smithy shape ``com.amazonaws.outposts#PaymentOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

PaymentOption: TypeAlias = Literal[
    "ALL_UPFRONT",
    "NO_UPFRONT",
    "PARTIAL_UPFRONT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL_UPFRONT",
        "NO_UPFRONT",
        "PARTIAL_UPFRONT",
    )
)


def serialize_json(value: PaymentOption) -> str:
    return value


def deserialize_json(data: str) -> PaymentOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PaymentOption value: {data!r}")
    return cast(PaymentOption, data)
