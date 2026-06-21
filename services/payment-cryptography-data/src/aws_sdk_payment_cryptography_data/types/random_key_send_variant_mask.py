"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#RandomKeySendVariantMask``."""

from typing import Literal, TypeAlias, cast

RandomKeySendVariantMask: TypeAlias = Literal[
    "VARIANT_MASK_82C0",
    "VARIANT_MASK_82",
]


# --- restJson1 ser/de ---
def serialize_json(value: RandomKeySendVariantMask) -> str:
    return value


def deserialize_json(data: str) -> RandomKeySendVariantMask:
    return cast(RandomKeySendVariantMask, data)
