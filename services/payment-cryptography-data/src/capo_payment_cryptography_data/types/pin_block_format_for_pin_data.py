"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#PinBlockFormatForPinData``."""

from typing import Literal, TypeAlias, cast

PinBlockFormatForPinData: TypeAlias = Literal[
    "ISO_FORMAT_0",
    "ISO_FORMAT_1",
    "ISO_FORMAT_3",
    "ISO_FORMAT_4",
]


# --- restJson1 ser/de ---
def serialize_json(value: PinBlockFormatForPinData) -> str:
    return value


def deserialize_json(data: str) -> PinBlockFormatForPinData:
    return cast(PinBlockFormatForPinData, data)
