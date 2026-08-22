"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.tag

TagList: TypeAlias = list["capo_bedrock_data_automation.types.tag.Tag"]


# --- restJson1 ser/de ---
def serialize_json(value: TagList) -> list:
    import capo_bedrock_data_automation.types.tag

    out: list = []
    for item in value:
        out.append(capo_bedrock_data_automation.types.tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> TagList:
    import capo_bedrock_data_automation.types.tag

    out: TagList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_data_automation.types.tag.deserialize_json(item))
    return out
