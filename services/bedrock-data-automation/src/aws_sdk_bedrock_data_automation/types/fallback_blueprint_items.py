"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#FallbackBlueprintItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.blueprint_item

FallbackBlueprintItems: TypeAlias = list[
    "aws_sdk_bedrock_data_automation.types.blueprint_item.BlueprintItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: FallbackBlueprintItems) -> list:
    import aws_sdk_bedrock_data_automation.types.blueprint_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_data_automation.types.blueprint_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FallbackBlueprintItems:
    import aws_sdk_bedrock_data_automation.types.blueprint_item

    out: FallbackBlueprintItems = []
    for item in data:
        out.append(
            aws_sdk_bedrock_data_automation.types.blueprint_item.deserialize_json(item)
        )
    return out
