"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#PaddingType``."""

from typing import Literal, TypeAlias, cast

PaddingType: TypeAlias = Literal[
    "PKCS1",
    "OAEP_SHA1",
    "OAEP_SHA256",
    "OAEP_SHA512",
]


# --- restJson1 ser/de ---
def serialize_json(value: PaddingType) -> str:
    return value


def deserialize_json(data: str) -> PaddingType:
    return cast(PaddingType, data)
