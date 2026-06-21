"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#PinBlockFormatForEmvPinChange``."""

from typing import Literal, TypeAlias, cast

PinBlockFormatForEmvPinChange: TypeAlias = Literal[
    "ISO_FORMAT_0",
    "ISO_FORMAT_1",
    "ISO_FORMAT_3",
]


# --- restJson1 ser/de ---
def serialize_json(value: PinBlockFormatForEmvPinChange) -> str:
    return value


def deserialize_json(data: str) -> PinBlockFormatForEmvPinChange:
    return cast(PinBlockFormatForEmvPinChange, data)
