"""Generated from Smithy shape ``com.amazonaws.connect#TaskTemplateFieldType``."""

from typing import Literal, TypeAlias, cast

TaskTemplateFieldType: TypeAlias = Literal[
    "NAME",
    "DESCRIPTION",
    "SCHEDULED_TIME",
    "QUICK_CONNECT",
    "URL",
    "NUMBER",
    "TEXT",
    "TEXT_AREA",
    "DATE_TIME",
    "BOOLEAN",
    "SINGLE_SELECT",
    "EMAIL",
    "SELF_ASSIGN",
    "EXPIRY_DURATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskTemplateFieldType) -> str:
    return value


def deserialize_json(data: str) -> TaskTemplateFieldType:
    return cast(TaskTemplateFieldType, data)
