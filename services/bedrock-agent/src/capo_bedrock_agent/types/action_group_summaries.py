"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ActionGroupSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.action_group_summary

ActionGroupSummaries: TypeAlias = list[
    "capo_bedrock_agent.types.action_group_summary.ActionGroupSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionGroupSummaries) -> list:
    import capo_bedrock_agent.types.action_group_summary

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent.types.action_group_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActionGroupSummaries:
    import capo_bedrock_agent.types.action_group_summary

    out: ActionGroupSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agent.types.action_group_summary.deserialize_json(item))
    return out
