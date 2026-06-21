"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ImportLensStatus``."""

from typing import Literal, TypeAlias, cast

ImportLensStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETE",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: ImportLensStatus) -> str:
    return value


def deserialize_json(data: str) -> ImportLensStatus:
    return cast(ImportLensStatus, data)
