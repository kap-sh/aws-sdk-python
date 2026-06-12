"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#MacAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_payment_cryptography_data.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "ISO9797_ALGORITHM1",
        "ISO9797_ALGORITHM3",
        "CMAC",
        "HMAC",
        "HMAC_SHA224",
        "HMAC_SHA256",
        "HMAC_SHA384",
        "HMAC_SHA512",
        "AS2805_4_1",
    )
)


def serialize_json(value: MacAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> MacAlgorithm:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MacAlgorithm value: {data!r}")
    return cast(MacAlgorithm, data)
