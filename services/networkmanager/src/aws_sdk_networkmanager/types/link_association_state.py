"""Generated from Smithy shape ``com.amazonaws.networkmanager#LinkAssociationState``."""

from typing import Literal, TypeAlias, cast

LinkAssociationState: TypeAlias = Literal[
    "PENDING",
    "AVAILABLE",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: LinkAssociationState) -> str:
    return value


def deserialize_json(data: str) -> LinkAssociationState:
    return cast(LinkAssociationState, data)
