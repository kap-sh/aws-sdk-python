"""Generated from Smithy shape ``com.amazonaws.emrcontainers#TemplateParameterDataType``."""

from typing import Literal, TypeAlias, cast

TemplateParameterDataType: TypeAlias = Literal[
    "NUMBER",
    "STRING",
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateParameterDataType) -> str:
    return value


def deserialize_json(data: str) -> TemplateParameterDataType:
    return cast(TemplateParameterDataType, data)
