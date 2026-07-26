"""Generated from Smithy shape ``com.amazonaws.controlcatalog#MappingTypeFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controlcatalog.types.mapping_type

MappingTypeFilterList: TypeAlias = list[
    "capo_controlcatalog.types.mapping_type.MappingType"
]


# --- restJson1 ser/de ---
def serialize_json(value: MappingTypeFilterList) -> list:
    import capo_controlcatalog.types.mapping_type

    out: list = []
    for item in value:
        out.append(capo_controlcatalog.types.mapping_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> MappingTypeFilterList:
    import capo_controlcatalog.types.mapping_type

    out: MappingTypeFilterList = []
    for item in data:
        out.append(capo_controlcatalog.types.mapping_type.deserialize_json(item))
    return out
