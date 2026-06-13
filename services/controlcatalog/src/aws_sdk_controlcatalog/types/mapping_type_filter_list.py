"""Generated from Smithy shape ``com.amazonaws.controlcatalog#MappingTypeFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.mapping_type

MappingTypeFilterList: TypeAlias = list[
    "aws_sdk_controlcatalog.types.mapping_type.MappingType"
]


# --- restJson1 ser/de ---
def serialize_json(value: MappingTypeFilterList) -> list:
    import aws_sdk_controlcatalog.types.mapping_type

    out: list = []
    for item in value:
        out.append(aws_sdk_controlcatalog.types.mapping_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> MappingTypeFilterList:
    import aws_sdk_controlcatalog.types.mapping_type

    out: MappingTypeFilterList = []
    for item in data:
        out.append(aws_sdk_controlcatalog.types.mapping_type.deserialize_json(item))
    return out
