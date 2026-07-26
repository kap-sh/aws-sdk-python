"""Generated from Smithy shape ``com.amazonaws.connect#ValidationEnumValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.string

ValidationEnumValues: TypeAlias = list["capo_connect.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationEnumValues) -> list:
    return list(value)


def deserialize_json(data: list) -> ValidationEnumValues:
    return list(data)
