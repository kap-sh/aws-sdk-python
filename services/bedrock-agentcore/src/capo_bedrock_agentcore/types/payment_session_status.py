"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentSessionStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a payment session.</p>"""
PaymentSessionStatus: TypeAlias = Literal[
    "ACTIVE",
    "EXPIRED",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PaymentSessionStatus) -> str:
    return value


def deserialize_json(data: str) -> PaymentSessionStatus:
    return cast(PaymentSessionStatus, data)
