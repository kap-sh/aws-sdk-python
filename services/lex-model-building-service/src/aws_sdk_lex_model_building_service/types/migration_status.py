"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#MigrationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_model_building_service.errors import DeserializationError

MigrationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "COMPLETED",
        "FAILED",
    )
)


def serialize_json(value: MigrationStatus) -> str:
    return value


def deserialize_json(data: str) -> MigrationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MigrationStatus value: {data!r}")
    return cast(MigrationStatus, data)
