"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#PinBlockFormatForEmvPinChange``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_payment_cryptography_data.errors import DeserializationError

PinBlockFormatForEmvPinChange: TypeAlias = Literal[
    "ISO_FORMAT_0",
    "ISO_FORMAT_1",
    "ISO_FORMAT_3",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ISO_FORMAT_0",
        "ISO_FORMAT_1",
        "ISO_FORMAT_3",
    )
)


def serialize_json(value: PinBlockFormatForEmvPinChange) -> str:
    return value


def deserialize_json(data: str) -> PinBlockFormatForEmvPinChange:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PinBlockFormatForEmvPinChange value: {data!r}"
        )
    return cast(PinBlockFormatForEmvPinChange, data)
