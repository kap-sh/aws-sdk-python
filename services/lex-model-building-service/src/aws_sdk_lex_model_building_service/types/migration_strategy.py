"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#MigrationStrategy``."""

from typing import Literal, TypeAlias, cast

MigrationStrategy: TypeAlias = Literal[
    "CREATE_NEW",
    "UPDATE_EXISTING",
]


# --- restJson1 ser/de ---
def serialize_json(value: MigrationStrategy) -> str:
    return value


def deserialize_json(data: str) -> MigrationStrategy:
    return cast(MigrationStrategy, data)
