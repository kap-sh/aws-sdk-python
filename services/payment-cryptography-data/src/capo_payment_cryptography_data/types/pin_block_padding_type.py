"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#PinBlockPaddingType``."""

from typing import Literal, TypeAlias, cast

PinBlockPaddingType: TypeAlias = Literal[
    "NO_PADDING",
    "ISO_IEC_7816_4",
]


# --- restJson1 ser/de ---
def serialize_json(value: PinBlockPaddingType) -> str:
    return value


def deserialize_json(data: str) -> PinBlockPaddingType:
    return cast(PinBlockPaddingType, data)
