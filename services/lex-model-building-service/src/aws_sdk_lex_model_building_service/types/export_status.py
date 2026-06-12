"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#ExportStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_model_building_service.errors import DeserializationError

ExportStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "READY",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "READY",
        "FAILED",
    )
)


def serialize_json(value: ExportStatus) -> str:
    return value


def deserialize_json(data: str) -> ExportStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExportStatus value: {data!r}")
    return cast(ExportStatus, data)
