"""Generated from Smithy shape ``com.amazonaws.rdsdata#Records``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rds_data.types.record

Records: TypeAlias = list["capo_rds_data.types.record.Record"]


# --- restJson1 ser/de ---
def serialize_json(value: Records) -> list:
    import capo_rds_data.types.record

    out: list = []
    for item in value:
        out.append(capo_rds_data.types.record.serialize_json(item))
    return out


def deserialize_json(data: list) -> Records:
    import capo_rds_data.types.record

    out: Records = []
    for item in data:
        out.append(capo_rds_data.types.record.deserialize_json(item))
    return out
