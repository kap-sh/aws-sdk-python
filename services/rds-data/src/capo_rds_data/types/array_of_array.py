"""Generated from Smithy shape ``com.amazonaws.rdsdata#ArrayOfArray``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rds_data.types.array_value

ArrayOfArray: TypeAlias = list["capo_rds_data.types.array_value.ArrayValue | None"]


# --- restJson1 ser/de ---
def serialize_json(value: ArrayOfArray) -> list:
    import capo_rds_data.types.array_value

    out: list = []
    for item in value:
        if item is None:
            out.append(None)
            continue
        out.append(capo_rds_data.types.array_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> ArrayOfArray:
    import capo_rds_data.types.array_value

    out: ArrayOfArray = []
    for item in data:
        if item is None:
            out.append(None)
            continue
        out.append(capo_rds_data.types.array_value.deserialize_json(item))
    return out
