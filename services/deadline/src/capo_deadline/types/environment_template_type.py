"""Generated from Smithy shape ``com.amazonaws.deadline#EnvironmentTemplateType``."""

from typing import Literal, TypeAlias, cast

EnvironmentTemplateType: TypeAlias = Literal[
    "JSON",
    "YAML",
]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentTemplateType) -> str:
    return value


def deserialize_json(data: str) -> EnvironmentTemplateType:
    return cast(EnvironmentTemplateType, data)
