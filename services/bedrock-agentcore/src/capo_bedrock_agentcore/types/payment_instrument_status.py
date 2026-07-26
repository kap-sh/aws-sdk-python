"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentInstrumentStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a payment instrument.</p>"""
PaymentInstrumentStatus: TypeAlias = Literal[
    "INITIATED",
    "ACTIVE",
    "FAILED",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PaymentInstrumentStatus) -> str:
    return value


def deserialize_json(data: str) -> PaymentInstrumentStatus:
    return cast(PaymentInstrumentStatus, data)
