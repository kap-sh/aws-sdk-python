"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#EntityIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.entity_id

EntityIdList: TypeAlias = list["capo_bedrock_data_automation.types.entity_id.EntityId"]


# --- restJson1 ser/de ---
def serialize_json(value: EntityIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> EntityIdList:
    return [item for item in data if item is not None]
