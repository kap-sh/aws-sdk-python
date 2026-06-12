"""Generated from Smithy shape ``com.amazonaws.connect#ValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.string

ValueList: TypeAlias = list["aws_sdk_connect.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> ValueList:
    return list(data)
