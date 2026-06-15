"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RegistrySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.registry_summary

RegistrySummaryList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.registry_summary.RegistrySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RegistrySummaryList) -> list:
    import aws_sdk_bedrock_agentcore_control.types.registry_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.registry_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RegistrySummaryList:
    import aws_sdk_bedrock_agentcore_control.types.registry_summary

    out: RegistrySummaryList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.registry_summary.deserialize_json(
                item
            )
        )
    return out
