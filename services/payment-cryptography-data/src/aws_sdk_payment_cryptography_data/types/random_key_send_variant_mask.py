"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#RandomKeySendVariantMask``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_payment_cryptography_data.errors import DeserializationError

RandomKeySendVariantMask: TypeAlias = Literal[
    "VARIANT_MASK_82C0",
    "VARIANT_MASK_82",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VARIANT_MASK_82C0",
        "VARIANT_MASK_82",
    )
)


def serialize_json(value: RandomKeySendVariantMask) -> str:
    return value


def deserialize_json(data: str) -> RandomKeySendVariantMask:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RandomKeySendVariantMask value: {data!r}")
    return cast(RandomKeySendVariantMask, data)
