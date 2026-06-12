"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#PinBlockFormatForPinData``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_payment_cryptography_data.errors import DeserializationError

PinBlockFormatForPinData: TypeAlias = Literal[
    "ISO_FORMAT_0",
    "ISO_FORMAT_1",
    "ISO_FORMAT_3",
    "ISO_FORMAT_4",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ISO_FORMAT_0",
        "ISO_FORMAT_1",
        "ISO_FORMAT_3",
        "ISO_FORMAT_4",
    )
)


def serialize_json(value: PinBlockFormatForPinData) -> str:
    return value


def deserialize_json(data: str) -> PinBlockFormatForPinData:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PinBlockFormatForPinData value: {data!r}")
    return cast(PinBlockFormatForPinData, data)
