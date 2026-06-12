"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#ExportType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_model_building_service.errors import DeserializationError

ExportType: TypeAlias = Literal[
    "ALEXA_SKILLS_KIT",
    "LEX",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALEXA_SKILLS_KIT",
        "LEX",
    )
)


def serialize_json(value: ExportType) -> str:
    return value


def deserialize_json(data: str) -> ExportType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExportType value: {data!r}")
    return cast(ExportType, data)
