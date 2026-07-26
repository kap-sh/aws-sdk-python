"""Generated from Smithy shape ``com.amazonaws.qbusiness#DataSourceIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.data_source_id

DataSourceIds: TypeAlias = list["capo_qbusiness.types.data_source_id.DataSourceId"]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceIds) -> list:
    return list(value)


def deserialize_json(data: list) -> DataSourceIds:
    return list(data)
