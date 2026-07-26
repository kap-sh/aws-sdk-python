"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#SyncAction``."""

from typing import Literal, TypeAlias, cast

SyncAction: TypeAlias = Literal[
    "START_SYNC",
    "NO_ACTION",
]


# --- restJson1 ser/de ---
def serialize_json(value: SyncAction) -> str:
    return value


def deserialize_json(data: str) -> SyncAction:
    return cast(SyncAction, data)
