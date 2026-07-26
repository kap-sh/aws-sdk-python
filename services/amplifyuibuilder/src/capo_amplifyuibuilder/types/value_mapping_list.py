"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ValueMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.value_mapping

ValueMappingList: TypeAlias = list[
    "capo_amplifyuibuilder.types.value_mapping.ValueMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValueMappingList) -> list:
    import capo_amplifyuibuilder.types.value_mapping

    out: list = []
    for item in value:
        out.append(capo_amplifyuibuilder.types.value_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> ValueMappingList:
    import capo_amplifyuibuilder.types.value_mapping

    out: ValueMappingList = []
    for item in data:
        out.append(capo_amplifyuibuilder.types.value_mapping.deserialize_json(item))
    return out
