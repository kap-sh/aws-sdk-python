"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#MigrationAlertType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_model_building_service.errors import DeserializationError

MigrationAlertType: TypeAlias = Literal[
    "ERROR",
    "WARN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ERROR",
        "WARN",
    )
)


def serialize_json(value: MigrationAlertType) -> str:
    return value


def deserialize_json(data: str) -> MigrationAlertType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MigrationAlertType value: {data!r}")
    return cast(MigrationAlertType, data)
