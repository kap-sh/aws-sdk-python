"""Generated from Smithy shape ``com.amazonaws.connect#DataSetIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.data_set_id

DataSetIds: TypeAlias = list["capo_connect.types.data_set_id.DataSetId"]


# --- restJson1 ser/de ---
def serialize_json(value: DataSetIds) -> list:
    return list(value)


def deserialize_json(data: list) -> DataSetIds:
    return list(data)
