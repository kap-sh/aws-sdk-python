"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#MacAlgorithm``."""

from typing import Literal, TypeAlias, cast

MacAlgorithm: TypeAlias = Literal[
    "ISO9797_ALGORITHM1",
    "ISO9797_ALGORITHM3",
    "CMAC",
    "HMAC",
    "HMAC_SHA224",
    "HMAC_SHA256",
    "HMAC_SHA384",
    "HMAC_SHA512",
    "AS2805_4_1",
]


# --- restJson1 ser/de ---
def serialize_json(value: MacAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> MacAlgorithm:
    return cast(MacAlgorithm, data)
