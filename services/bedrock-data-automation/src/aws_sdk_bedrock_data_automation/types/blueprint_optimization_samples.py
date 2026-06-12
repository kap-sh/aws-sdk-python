"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#BlueprintOptimizationSamples``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.blueprint_optimization_sample

BlueprintOptimizationSamples: TypeAlias = list[
    "aws_sdk_bedrock_data_automation.types.blueprint_optimization_sample.BlueprintOptimizationSample"
]


# --- restJson1 ser/de ---
def serialize_json(value: BlueprintOptimizationSamples) -> list:
    import aws_sdk_bedrock_data_automation.types.blueprint_optimization_sample

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_data_automation.types.blueprint_optimization_sample.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BlueprintOptimizationSamples:
    import aws_sdk_bedrock_data_automation.types.blueprint_optimization_sample

    out: BlueprintOptimizationSamples = []
    for item in data:
        out.append(
            aws_sdk_bedrock_data_automation.types.blueprint_optimization_sample.deserialize_json(
                item
            )
        )
    return out
