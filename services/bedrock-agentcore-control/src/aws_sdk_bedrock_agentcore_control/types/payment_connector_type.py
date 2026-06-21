"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PaymentConnectorType``."""

from typing import Literal, TypeAlias, cast

PaymentConnectorType: TypeAlias = Literal[
    "CoinbaseCDP",
    "StripePrivy",
]


# --- restJson1 ser/de ---
def serialize_json(value: PaymentConnectorType) -> str:
    return value


def deserialize_json(data: str) -> PaymentConnectorType:
    return cast(PaymentConnectorType, data)
