"""Generated from Smithy shape ``com.amazonaws.wickr#Unames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string

Unames: TypeAlias = list["aws_sdk_wickr.types.generic_string.GenericString"]


# --- restJson1 ser/de ---
def serialize_json(value: Unames) -> list:
    return list(value)


def deserialize_json(data: list) -> Unames:
    return list(data)
