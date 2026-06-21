"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PaymentManagerStatus``."""

from typing import Literal, TypeAlias, cast

PaymentManagerStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "DELETING",
    "READY",
    "CREATE_FAILED",
    "UPDATE_FAILED",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PaymentManagerStatus) -> str:
    return value


def deserialize_json(data: str) -> PaymentManagerStatus:
    return cast(PaymentManagerStatus, data)
