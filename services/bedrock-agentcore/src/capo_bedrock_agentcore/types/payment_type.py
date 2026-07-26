"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentType``."""

from typing import Literal, TypeAlias, cast

"""<p>Payment type enum.</p>"""
PaymentType: TypeAlias = Literal["CRYPTO_X402",]


# --- restJson1 ser/de ---
def serialize_json(value: PaymentType) -> str:
    return value


def deserialize_json(data: str) -> PaymentType:
    return cast(PaymentType, data)
