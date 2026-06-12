"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#MigrationStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_model_building_service.errors import DeserializationError

MigrationStrategy: TypeAlias = Literal[
    "CREATE_NEW",
    "UPDATE_EXISTING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_NEW",
        "UPDATE_EXISTING",
    )
)


def serialize_json(value: MigrationStrategy) -> str:
    return value


def deserialize_json(data: str) -> MigrationStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MigrationStrategy value: {data!r}")
    return cast(MigrationStrategy, data)
