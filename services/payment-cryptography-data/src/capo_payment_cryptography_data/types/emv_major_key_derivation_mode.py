"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#EmvMajorKeyDerivationMode``."""

from typing import Literal, TypeAlias, cast

EmvMajorKeyDerivationMode: TypeAlias = Literal[
    "EMV_OPTION_A",
    "EMV_OPTION_B",
]


# --- restJson1 ser/de ---
def serialize_json(value: EmvMajorKeyDerivationMode) -> str:
    return value


def deserialize_json(data: str) -> EmvMajorKeyDerivationMode:
    return cast(EmvMajorKeyDerivationMode, data)
