"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#MigrationSortAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_model_building_service.errors import DeserializationError

MigrationSortAttribute: TypeAlias = Literal[
    "V1_BOT_NAME",
    "MIGRATION_DATE_TIME",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "V1_BOT_NAME",
        "MIGRATION_DATE_TIME",
    )
)


def serialize_json(value: MigrationSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> MigrationSortAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MigrationSortAttribute value: {data!r}")
    return cast(MigrationSortAttribute, data)
