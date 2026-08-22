"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_data_automation_runtime.types.tag

TagList: TypeAlias = list["capo_bedrock_data_automation_runtime.types.tag.Tag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagList) -> list:
    import capo_bedrock_data_automation_runtime.types.tag

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_data_automation_runtime.types.tag.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TagList:
    import capo_bedrock_data_automation_runtime.types.tag

    out: TagList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_data_automation_runtime.types.tag.deserialize_aws_json_1_1(
                item
            )
        )
    return out
