"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#PinBlockLengthPosition``."""

from typing import Literal, TypeAlias, cast

PinBlockLengthPosition: TypeAlias = Literal[
    "NONE",
    "FRONT_OF_PIN_BLOCK",
]


# --- restJson1 ser/de ---
def serialize_json(value: PinBlockLengthPosition) -> str:
    return value


def deserialize_json(data: str) -> PinBlockLengthPosition:
    return cast(PinBlockLengthPosition, data)
