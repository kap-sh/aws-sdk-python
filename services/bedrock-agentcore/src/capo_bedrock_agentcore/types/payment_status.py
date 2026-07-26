"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Transaction status enum.</p>"""
PaymentStatus: TypeAlias = Literal["PROOF_GENERATED",]


# --- restJson1 ser/de ---
def serialize_json(value: PaymentStatus) -> str:
    return value


def deserialize_json(data: str) -> PaymentStatus:
    return cast(PaymentStatus, data)
