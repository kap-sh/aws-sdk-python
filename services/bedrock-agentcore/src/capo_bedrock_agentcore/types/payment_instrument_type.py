"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentInstrumentType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of payment instrument.</p>"""
PaymentInstrumentType: TypeAlias = Literal["EMBEDDED_CRYPTO_WALLET",]


# --- restJson1 ser/de ---
def serialize_json(value: PaymentInstrumentType) -> str:
    return value


def deserialize_json(data: str) -> PaymentInstrumentType:
    return cast(PaymentInstrumentType, data)
