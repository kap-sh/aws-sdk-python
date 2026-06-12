"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#PinBlockLengthPosition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_payment_cryptography_data.errors import DeserializationError

PinBlockLengthPosition: TypeAlias = Literal[
    "NONE",
    "FRONT_OF_PIN_BLOCK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "FRONT_OF_PIN_BLOCK",
    )
)


def serialize_json(value: PinBlockLengthPosition) -> str:
    return value


def deserialize_json(data: str) -> PinBlockLengthPosition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PinBlockLengthPosition value: {data!r}")
    return cast(PinBlockLengthPosition, data)
