"""Generated from Smithy shape ``com.amazonaws.opensearch#ReservedInstancePaymentOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

ReservedInstancePaymentOption: TypeAlias = Literal[
    "ALL_UPFRONT",
    "PARTIAL_UPFRONT",
    "NO_UPFRONT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL_UPFRONT",
        "PARTIAL_UPFRONT",
        "NO_UPFRONT",
    )
)


def serialize_json(value: ReservedInstancePaymentOption) -> str:
    return value


def deserialize_json(data: str) -> ReservedInstancePaymentOption:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ReservedInstancePaymentOption value: {data!r}"
        )
    return cast(ReservedInstancePaymentOption, data)
