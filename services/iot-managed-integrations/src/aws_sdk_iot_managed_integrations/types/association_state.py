"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#AssociationState``."""

from typing import Literal, TypeAlias, cast

AssociationState: TypeAlias = Literal[
    "ASSOCIATION_IN_PROGRESS",
    "ASSOCIATION_FAILED",
    "ASSOCIATION_SUCCEEDED",
    "ASSOCIATION_DELETING",
    "REFRESH_TOKEN_EXPIRED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociationState) -> str:
    return value


def deserialize_json(data: str) -> AssociationState:
    return cast(AssociationState, data)
