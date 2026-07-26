"""Generated from Smithy shape ``com.amazonaws.qbusiness#DataAccessors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.data_accessor

DataAccessors: TypeAlias = list["capo_qbusiness.types.data_accessor.DataAccessor"]


# --- restJson1 ser/de ---
def serialize_json(value: DataAccessors) -> list:
    import capo_qbusiness.types.data_accessor

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.data_accessor.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataAccessors:
    import capo_qbusiness.types.data_accessor

    out: DataAccessors = []
    for item in data:
        out.append(capo_qbusiness.types.data_accessor.deserialize_json(item))
    return out
