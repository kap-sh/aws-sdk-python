"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#MajorKeyDerivationMode``."""

from typing import Literal, TypeAlias, cast

MajorKeyDerivationMode: TypeAlias = Literal[
    "EMV_OPTION_A",
    "EMV_OPTION_B",
]


# --- restJson1 ser/de ---
def serialize_json(value: MajorKeyDerivationMode) -> str:
    return value


def deserialize_json(data: str) -> MajorKeyDerivationMode:
    return cast(MajorKeyDerivationMode, data)
