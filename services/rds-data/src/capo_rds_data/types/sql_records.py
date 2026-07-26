"""Generated from Smithy shape ``com.amazonaws.rdsdata#SqlRecords``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rds_data.types.field_list

SqlRecords: TypeAlias = list["capo_rds_data.types.field_list.FieldList"]


# --- restJson1 ser/de ---
def serialize_json(value: SqlRecords) -> list:
    import capo_rds_data.types.field_list

    out: list = []
    for item in value:
        out.append(capo_rds_data.types.field_list.serialize_json(item))
    return out


def deserialize_json(data: list) -> SqlRecords:
    import capo_rds_data.types.field_list

    out: SqlRecords = []
    for item in data:
        out.append(capo_rds_data.types.field_list.deserialize_json(item))
    return out
