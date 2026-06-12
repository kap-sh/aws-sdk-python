"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#TabularPropertyValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.tabular_property_value

TabularPropertyValues: TypeAlias = list[
    "aws_sdk_iottwinmaker.types.tabular_property_value.TabularPropertyValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: TabularPropertyValues) -> list:
    import aws_sdk_iottwinmaker.types.tabular_property_value

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iottwinmaker.types.tabular_property_value.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TabularPropertyValues:
    import aws_sdk_iottwinmaker.types.tabular_property_value

    out: TabularPropertyValues = []
    for item in data:
        out.append(
            aws_sdk_iottwinmaker.types.tabular_property_value.deserialize_json(item)
        )
    return out
