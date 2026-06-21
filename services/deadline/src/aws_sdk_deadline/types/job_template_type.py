"""Generated from Smithy shape ``com.amazonaws.deadline#JobTemplateType``."""

from typing import Literal, TypeAlias, cast

JobTemplateType: TypeAlias = Literal[
    "JSON",
    "YAML",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobTemplateType) -> str:
    return value


def deserialize_json(data: str) -> JobTemplateType:
    return cast(JobTemplateType, data)
