"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertyNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.name

PropertyNames: TypeAlias = list["aws_sdk_iottwinmaker.types.name.Name"]


# --- restJson1 ser/de ---
def serialize_json(value: PropertyNames) -> list:
    return list(value)


def deserialize_json(data: list) -> PropertyNames:
    return list(data)
