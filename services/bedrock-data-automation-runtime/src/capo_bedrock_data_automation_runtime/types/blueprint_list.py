"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#BlueprintList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_data_automation_runtime.types.blueprint

BlueprintList: TypeAlias = list[
    "capo_bedrock_data_automation_runtime.types.blueprint.Blueprint"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlueprintList) -> list:
    import capo_bedrock_data_automation_runtime.types.blueprint

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_data_automation_runtime.types.blueprint.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BlueprintList:
    import capo_bedrock_data_automation_runtime.types.blueprint

    out: BlueprintList = []
    for item in data:
        out.append(
            capo_bedrock_data_automation_runtime.types.blueprint.deserialize_aws_json_1_1(
                item
            )
        )
    return out
