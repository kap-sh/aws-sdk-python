"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ComponentFormat``."""

from typing import Literal, TypeAlias, cast

ComponentFormat: TypeAlias = Literal["SHELL",]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentFormat) -> str:
    return value


def deserialize_json(data: str) -> ComponentFormat:
    return cast(ComponentFormat, data)
