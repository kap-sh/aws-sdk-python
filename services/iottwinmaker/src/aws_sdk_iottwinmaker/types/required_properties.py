"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#RequiredProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.name

RequiredProperties: TypeAlias = list["aws_sdk_iottwinmaker.types.name.Name"]


# --- restJson1 ser/de ---
def serialize_json(value: RequiredProperties) -> list:
    return list(value)


def deserialize_json(data: list) -> RequiredProperties:
    return list(data)
