"""Generated from Smithy shape ``com.amazonaws.resiliencehub#Row``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.string255

Row: TypeAlias = list["aws_sdk_resiliencehub.types.string255.String255"]


# --- restJson1 ser/de ---
def serialize_json(value: Row) -> list:
    return list(value)


def deserialize_json(data: list) -> Row:
    return list(data)
