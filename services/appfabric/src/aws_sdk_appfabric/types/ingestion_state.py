"""Generated from Smithy shape ``com.amazonaws.appfabric#IngestionState``."""

from typing import Literal, TypeAlias, cast

IngestionState: TypeAlias = Literal[
    "enabled",
    "disabled",
]


# --- restJson1 ser/de ---
def serialize_json(value: IngestionState) -> str:
    return value


def deserialize_json(data: str) -> IngestionState:
    return cast(IngestionState, data)
