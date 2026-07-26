"""Generated from Smithy shape ``com.amazonaws.efs#DeletionMode``."""

from typing import Literal, TypeAlias, cast

DeletionMode: TypeAlias = Literal[
    "ALL_CONFIGURATIONS",
    "LOCAL_CONFIGURATION_ONLY",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeletionMode) -> str:
    return value


def deserialize_json(data: str) -> DeletionMode:
    return cast(DeletionMode, data)
