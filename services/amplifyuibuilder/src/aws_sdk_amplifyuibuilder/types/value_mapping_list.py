"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ValueMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.value_mapping

ValueMappingList: TypeAlias = list[
    "aws_sdk_amplifyuibuilder.types.value_mapping.ValueMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValueMappingList) -> list:
    import aws_sdk_amplifyuibuilder.types.value_mapping

    out: list = []
    for item in value:
        out.append(aws_sdk_amplifyuibuilder.types.value_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> ValueMappingList:
    import aws_sdk_amplifyuibuilder.types.value_mapping

    out: ValueMappingList = []
    for item in data:
        out.append(aws_sdk_amplifyuibuilder.types.value_mapping.deserialize_json(item))
    return out
