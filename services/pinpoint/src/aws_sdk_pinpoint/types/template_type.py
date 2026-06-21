"""Generated from Smithy shape ``com.amazonaws.pinpoint#TemplateType``."""

from typing import Literal, TypeAlias, cast

TemplateType: TypeAlias = Literal[
    "EMAIL",
    "SMS",
    "VOICE",
    "PUSH",
    "INAPP",
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateType) -> str:
    return value


def deserialize_json(data: str) -> TemplateType:
    return cast(TemplateType, data)
