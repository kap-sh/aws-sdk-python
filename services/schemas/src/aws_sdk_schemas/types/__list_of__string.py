"""Generated from Smithy shape ``com.amazonaws.schemas#__listOf__string``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__string

__listOf__string: TypeAlias = list["aws_sdk_schemas.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOf__string) -> list:
    return list(value)


def deserialize_json(data: list) -> __listOf__string:
    return list(data)
