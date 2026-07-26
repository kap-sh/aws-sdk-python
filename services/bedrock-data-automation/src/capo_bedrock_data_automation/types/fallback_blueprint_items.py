"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#FallbackBlueprintItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.blueprint_item

FallbackBlueprintItems: TypeAlias = list[
    "capo_bedrock_data_automation.types.blueprint_item.BlueprintItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: FallbackBlueprintItems) -> list:
    import capo_bedrock_data_automation.types.blueprint_item

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_data_automation.types.blueprint_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FallbackBlueprintItems:
    import capo_bedrock_data_automation.types.blueprint_item

    out: FallbackBlueprintItems = []
    for item in data:
        out.append(
            capo_bedrock_data_automation.types.blueprint_item.deserialize_json(item)
        )
    return out
