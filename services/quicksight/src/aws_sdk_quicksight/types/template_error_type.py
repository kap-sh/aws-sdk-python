"""Generated from Smithy shape ``com.amazonaws.quicksight#TemplateErrorType``."""

from typing import Literal, TypeAlias, cast

TemplateErrorType: TypeAlias = Literal[
    "SOURCE_NOT_FOUND",
    "DATA_SET_NOT_FOUND",
    "INTERNAL_FAILURE",
    "ACCESS_DENIED",
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateErrorType) -> str:
    return value


def deserialize_json(data: str) -> TemplateErrorType:
    return cast(TemplateErrorType, data)
