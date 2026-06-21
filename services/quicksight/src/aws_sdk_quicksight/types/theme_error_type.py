"""Generated from Smithy shape ``com.amazonaws.quicksight#ThemeErrorType``."""

from typing import Literal, TypeAlias, cast

ThemeErrorType: TypeAlias = Literal["INTERNAL_FAILURE",]


# --- restJson1 ser/de ---
def serialize_json(value: ThemeErrorType) -> str:
    return value


def deserialize_json(data: str) -> ThemeErrorType:
    return cast(ThemeErrorType, data)
