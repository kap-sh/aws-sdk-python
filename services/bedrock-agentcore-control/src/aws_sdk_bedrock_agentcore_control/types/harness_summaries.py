"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.harness_summary

HarnessSummaries: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.harness_summary.HarnessSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessSummaries) -> list:
    import aws_sdk_bedrock_agentcore_control.types.harness_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.harness_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> HarnessSummaries:
    import aws_sdk_bedrock_agentcore_control.types.harness_summary

    out: HarnessSummaries = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.harness_summary.deserialize_json(
                item
            )
        )
    return out
