"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ActionGroupSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.action_group_summary

ActionGroupSummaries: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.action_group_summary.ActionGroupSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionGroupSummaries) -> list:
    import aws_sdk_bedrock_agent.types.action_group_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent.types.action_group_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ActionGroupSummaries:
    import aws_sdk_bedrock_agent.types.action_group_summary

    out: ActionGroupSummaries = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent.types.action_group_summary.deserialize_json(item)
        )
    return out
