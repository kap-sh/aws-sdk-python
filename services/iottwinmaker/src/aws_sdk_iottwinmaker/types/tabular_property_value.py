"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#TabularPropertyValue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.property_table_value

TabularPropertyValue: TypeAlias = list[
    "aws_sdk_iottwinmaker.types.property_table_value.PropertyTableValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: TabularPropertyValue) -> list:
    import aws_sdk_iottwinmaker.types.property_table_value

    out: list = []
    for item in value:
        out.append(aws_sdk_iottwinmaker.types.property_table_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> TabularPropertyValue:
    import aws_sdk_iottwinmaker.types.property_table_value

    out: TabularPropertyValue = []
    for item in data:
        out.append(
            aws_sdk_iottwinmaker.types.property_table_value.deserialize_json(item)
        )
    return out
