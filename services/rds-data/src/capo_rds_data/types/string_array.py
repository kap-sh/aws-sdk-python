"""Generated from Smithy shape ``com.amazonaws.rdsdata#StringArray``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rds_data.types.string

StringArray: TypeAlias = list["capo_rds_data.types.string.String | None"]


# --- restJson1 ser/de ---
def serialize_json(value: StringArray) -> list:
    return list(value)


def deserialize_json(data: list) -> StringArray:
    return list(data)
