"""Generated from Smithy shape ``com.amazonaws.connect#AttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.data_table_attribute

AttributeList: TypeAlias = list[
    "capo_connect.types.data_table_attribute.DataTableAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeList) -> list:
    import capo_connect.types.data_table_attribute

    out: list = []
    for item in value:
        out.append(capo_connect.types.data_table_attribute.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttributeList:
    import capo_connect.types.data_table_attribute

    out: AttributeList = []
    for item in data:
        out.append(capo_connect.types.data_table_attribute.deserialize_json(item))
    return out
