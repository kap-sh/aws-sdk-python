"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#DukptKeyVariant``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_payment_cryptography_data.errors import DeserializationError

DukptKeyVariant: TypeAlias = Literal[
    "BIDIRECTIONAL",
    "REQUEST",
    "RESPONSE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BIDIRECTIONAL",
        "REQUEST",
        "RESPONSE",
    )
)


def serialize_json(value: DukptKeyVariant) -> str:
    return value


def deserialize_json(data: str) -> DukptKeyVariant:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DukptKeyVariant value: {data!r}")
    return cast(DukptKeyVariant, data)
