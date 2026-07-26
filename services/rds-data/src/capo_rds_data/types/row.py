"""Generated from Smithy shape ``com.amazonaws.rdsdata#Row``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rds_data.types.value

Row: TypeAlias = list["capo_rds_data.types.value.Value"]


# --- restJson1 ser/de ---
def serialize_json(value: Row) -> list:
    import capo_rds_data.types.value

    out: list = []
    for item in value:
        out.append(capo_rds_data.types.value.serialize_json(item))
    return out


def deserialize_json(data: list) -> Row:
    import capo_rds_data.types.value

    out: Row = []
    for item in data:
        out.append(capo_rds_data.types.value.deserialize_json(item))
    return out
