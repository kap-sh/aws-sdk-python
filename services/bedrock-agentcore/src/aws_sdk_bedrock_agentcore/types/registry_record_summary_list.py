"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RegistryRecordSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.registry_record_summary

RegistryRecordSummaryList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore.types.registry_record_summary.RegistryRecordSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RegistryRecordSummaryList) -> list:
    import aws_sdk_bedrock_agentcore.types.registry_record_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore.types.registry_record_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RegistryRecordSummaryList:
    import aws_sdk_bedrock_agentcore.types.registry_record_summary

    out: RegistryRecordSummaryList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore.types.registry_record_summary.deserialize_json(
                item
            )
        )
    return out
