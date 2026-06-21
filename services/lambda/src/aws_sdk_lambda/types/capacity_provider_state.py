"""Generated from Smithy shape ``com.amazonaws.lambda#CapacityProviderState``."""

from typing import Literal, TypeAlias, cast

CapacityProviderState: TypeAlias = Literal[
    "Pending",
    "Active",
    "Failed",
    "Deleting",
]


# --- restJson1 ser/de ---
def serialize_json(value: CapacityProviderState) -> str:
    return value


def deserialize_json(data: str) -> CapacityProviderState:
    return cast(CapacityProviderState, data)
