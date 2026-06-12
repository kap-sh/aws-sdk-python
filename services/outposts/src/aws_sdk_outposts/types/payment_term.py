"""Generated from Smithy shape ``com.amazonaws.outposts#PaymentTerm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

PaymentTerm: TypeAlias = Literal[
    "THREE_YEARS",
    "ONE_YEAR",
    "FIVE_YEARS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "THREE_YEARS",
        "ONE_YEAR",
        "FIVE_YEARS",
    )
)


def serialize_json(value: PaymentTerm) -> str:
    return value


def deserialize_json(data: str) -> PaymentTerm:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PaymentTerm value: {data!r}")
    return cast(PaymentTerm, data)
