"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RegistryRecordSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.registry_record_summary

RegistryRecordSummaryList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.registry_record_summary.RegistryRecordSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RegistryRecordSummaryList) -> list:
    import capo_bedrock_agentcore_control.types.registry_record_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.registry_record_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RegistryRecordSummaryList:
    import capo_bedrock_agentcore_control.types.registry_record_summary

    out: RegistryRecordSummaryList = []
    for item in data:
        out.append(
            capo_bedrock_agentcore_control.types.registry_record_summary.deserialize_json(
                item
            )
        )
    return out
