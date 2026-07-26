"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#DukptDerivationType``."""

from typing import Literal, TypeAlias, cast

DukptDerivationType: TypeAlias = Literal[
    "TDES_2KEY",
    "TDES_3KEY",
    "AES_128",
    "AES_192",
    "AES_256",
]


# --- restJson1 ser/de ---
def serialize_json(value: DukptDerivationType) -> str:
    return value


def deserialize_json(data: str) -> DukptDerivationType:
    return cast(DukptDerivationType, data)
