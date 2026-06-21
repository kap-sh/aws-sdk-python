"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PaymentConnectorStatus``."""

from typing import Literal, TypeAlias, cast

PaymentConnectorStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "DELETING",
    "READY",
    "CREATE_FAILED",
    "UPDATE_FAILED",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PaymentConnectorStatus) -> str:
    return value


def deserialize_json(data: str) -> PaymentConnectorStatus:
    return cast(PaymentConnectorStatus, data)
