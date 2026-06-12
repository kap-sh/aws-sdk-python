"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#PinBlockPaddingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_payment_cryptography_data.errors import DeserializationError

PinBlockPaddingType: TypeAlias = Literal[
    "NO_PADDING",
    "ISO_IEC_7816_4",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_PADDING",
        "ISO_IEC_7816_4",
    )
)


def serialize_json(value: PinBlockPaddingType) -> str:
    return value


def deserialize_json(data: str) -> PinBlockPaddingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PinBlockPaddingType value: {data!r}")
    return cast(PinBlockPaddingType, data)
