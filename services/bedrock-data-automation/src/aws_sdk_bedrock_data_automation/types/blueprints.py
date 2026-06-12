"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#Blueprints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.blueprint_summary

Blueprints: TypeAlias = list[
    "aws_sdk_bedrock_data_automation.types.blueprint_summary.BlueprintSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: Blueprints) -> list:
    import aws_sdk_bedrock_data_automation.types.blueprint_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_data_automation.types.blueprint_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> Blueprints:
    import aws_sdk_bedrock_data_automation.types.blueprint_summary

    out: Blueprints = []
    for item in data:
        out.append(
            aws_sdk_bedrock_data_automation.types.blueprint_summary.deserialize_json(
                item
            )
        )
    return out
