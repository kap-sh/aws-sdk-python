"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#MigrationAlertType``."""

from typing import Literal, TypeAlias, cast

MigrationAlertType: TypeAlias = Literal[
    "ERROR",
    "WARN",
]


# --- restJson1 ser/de ---
def serialize_json(value: MigrationAlertType) -> str:
    return value


def deserialize_json(data: str) -> MigrationAlertType:
    return cast(MigrationAlertType, data)
