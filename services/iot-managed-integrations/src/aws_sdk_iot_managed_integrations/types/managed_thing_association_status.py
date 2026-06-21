"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ManagedThingAssociationStatus``."""

from typing import Literal, TypeAlias, cast

ManagedThingAssociationStatus: TypeAlias = Literal[
    "PRE_ASSOCIATED",
    "ASSOCIATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ManagedThingAssociationStatus) -> str:
    return value


def deserialize_json(data: str) -> ManagedThingAssociationStatus:
    return cast(ManagedThingAssociationStatus, data)
