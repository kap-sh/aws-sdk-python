"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#MigrationSortAttribute``."""

from typing import Literal, TypeAlias, cast

MigrationSortAttribute: TypeAlias = Literal[
    "V1_BOT_NAME",
    "MIGRATION_DATE_TIME",
]


# --- restJson1 ser/de ---
def serialize_json(value: MigrationSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> MigrationSortAttribute:
    return cast(MigrationSortAttribute, data)
