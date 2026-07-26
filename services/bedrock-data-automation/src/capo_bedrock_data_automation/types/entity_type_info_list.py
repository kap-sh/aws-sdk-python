"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#EntityTypeInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.entity_type_info

EntityTypeInfoList: TypeAlias = list[
    "capo_bedrock_data_automation.types.entity_type_info.EntityTypeInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: EntityTypeInfoList) -> list:
    import capo_bedrock_data_automation.types.entity_type_info

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_data_automation.types.entity_type_info.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EntityTypeInfoList:
    import capo_bedrock_data_automation.types.entity_type_info

    out: EntityTypeInfoList = []
    for item in data:
        out.append(
            capo_bedrock_data_automation.types.entity_type_info.deserialize_json(item)
        )
    return out
