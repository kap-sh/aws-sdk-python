"""Generated from Smithy shape ``com.amazonaws.ram#ResourceShareAssociationStatus``."""

from typing import Literal, TypeAlias, cast

ResourceShareAssociationStatus: TypeAlias = Literal[
    "ASSOCIATING",
    "ASSOCIATED",
    "FAILED",
    "DISASSOCIATING",
    "DISASSOCIATED",
    "SUSPENDED",
    "SUSPENDING",
    "RESTORING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceShareAssociationStatus) -> str:
    return value


def deserialize_json(data: str) -> ResourceShareAssociationStatus:
    return cast(ResourceShareAssociationStatus, data)
