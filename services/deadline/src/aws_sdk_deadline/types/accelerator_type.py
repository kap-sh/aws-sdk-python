"""Generated from Smithy shape ``com.amazonaws.deadline#AcceleratorType``."""

from typing import Literal, TypeAlias, cast

AcceleratorType: TypeAlias = Literal["gpu",]


# --- restJson1 ser/de ---
def serialize_json(value: AcceleratorType) -> str:
    return value


def deserialize_json(data: str) -> AcceleratorType:
    return cast(AcceleratorType, data)
