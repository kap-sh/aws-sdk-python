"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#ExportType``."""

from typing import Literal, TypeAlias, cast

ExportType: TypeAlias = Literal[
    "ALEXA_SKILLS_KIT",
    "LEX",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExportType) -> str:
    return value


def deserialize_json(data: str) -> ExportType:
    return cast(ExportType, data)
