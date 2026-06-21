"""Generated from Smithy shape ``com.amazonaws.securityir#PendingAction``."""

from typing import Literal, TypeAlias, cast

PendingAction: TypeAlias = Literal[
    "Customer",
    "None",
]


# --- restJson1 ser/de ---
def serialize_json(value: PendingAction) -> str:
    return value


def deserialize_json(data: str) -> PendingAction:
    return cast(PendingAction, data)
