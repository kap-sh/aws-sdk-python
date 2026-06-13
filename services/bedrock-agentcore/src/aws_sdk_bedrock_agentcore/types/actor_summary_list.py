"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ActorSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.actor_summary

ActorSummaryList: TypeAlias = list["aws_sdk_bedrock_agentcore.types.actor_summary.ActorSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: ActorSummaryList) -> list:
    import aws_sdk_bedrock_agentcore.types.actor_summary
    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agentcore.types.actor_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActorSummaryList:
    import aws_sdk_bedrock_agentcore.types.actor_summary
    out: ActorSummaryList = []
    for item in data:
        out.append(aws_sdk_bedrock_agentcore.types.actor_summary.deserialize_json(item))
    return out