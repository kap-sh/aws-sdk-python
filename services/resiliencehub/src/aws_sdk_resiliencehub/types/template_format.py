"""Generated from Smithy shape ``com.amazonaws.resiliencehub#TemplateFormat``."""

from typing import Literal, TypeAlias, cast

TemplateFormat: TypeAlias = Literal[
    "CfnYaml",
    "CfnJson",
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateFormat) -> str:
    return value


def deserialize_json(data: str) -> TemplateFormat:
    return cast(TemplateFormat, data)
