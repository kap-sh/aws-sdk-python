"""Generated from Smithy shape ``com.amazonaws.connect#AttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_attribute

AttributeList: TypeAlias = list[
    "aws_sdk_connect.types.data_table_attribute.DataTableAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeList) -> list:
    import aws_sdk_connect.types.data_table_attribute

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.data_table_attribute.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttributeList:
    import aws_sdk_connect.types.data_table_attribute

    out: AttributeList = []
    for item in data:
        out.append(aws_sdk_connect.types.data_table_attribute.deserialize_json(item))
    return out
