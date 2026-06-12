"""Generated from Smithy shape ``com.amazonaws.connect#AttributeIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_id

AttributeIds: TypeAlias = list["aws_sdk_connect.types.data_table_id.DataTableId"]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeIds) -> list:
    return list(value)


def deserialize_json(data: list) -> AttributeIds:
    return list(data)
