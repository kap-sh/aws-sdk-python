"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IdMappingTableInputSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.id_mapping_table_input_source

IdMappingTableInputSourceList: TypeAlias = list[
    "capo_cleanrooms.types.id_mapping_table_input_source.IdMappingTableInputSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingTableInputSourceList) -> list:
    import capo_cleanrooms.types.id_mapping_table_input_source

    out: list = []
    for item in value:
        out.append(
            capo_cleanrooms.types.id_mapping_table_input_source.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IdMappingTableInputSourceList:
    import capo_cleanrooms.types.id_mapping_table_input_source

    out: IdMappingTableInputSourceList = []
    for item in data:
        out.append(
            capo_cleanrooms.types.id_mapping_table_input_source.deserialize_json(item)
        )
    return out
