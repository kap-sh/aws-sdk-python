"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ResourceGroupState``."""

from typing import Literal, TypeAlias, cast

ResourceGroupState: TypeAlias = Literal[
    "CREATING",
    "CREATE_COMPLETE",
    "CREATE_FAILED",
    "UPDATING",
    "UPDATE_COMPLETE",
    "UPDATE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceGroupState) -> str:
    return value


def deserialize_json(data: str) -> ResourceGroupState:
    return cast(ResourceGroupState, data)
