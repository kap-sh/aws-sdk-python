"""Generated from Smithy shape ``com.amazonaws.databrew#ValidationMode``."""

from typing import Literal, TypeAlias, cast

ValidationMode: TypeAlias = Literal["CHECK_ALL",]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationMode) -> str:
    return value


def deserialize_json(data: str) -> ValidationMode:
    return cast(ValidationMode, data)
