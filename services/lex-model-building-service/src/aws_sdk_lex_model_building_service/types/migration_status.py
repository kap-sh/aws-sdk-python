"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#MigrationStatus``."""

from typing import Literal, TypeAlias, cast

MigrationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: MigrationStatus) -> str:
    return value


def deserialize_json(data: str) -> MigrationStatus:
    return cast(MigrationStatus, data)
