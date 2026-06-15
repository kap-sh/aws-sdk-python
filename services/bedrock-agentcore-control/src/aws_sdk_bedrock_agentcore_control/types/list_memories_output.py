"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListMemoriesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.memory_summary_list


class ListMemoriesOutput(TypedDict):
    memories: (
        "aws_sdk_bedrock_agentcore_control.types.memory_summary_list.MemorySummaryList"
    )
    """<p>The list of AgentCore Memory resource summaries.</p>"""
    next_token: NotRequired["str"]
    """<p>A token to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMemoriesOutput) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.memory_summary_list

    out["memories"] = (
        aws_sdk_bedrock_agentcore_control.types.memory_summary_list.serialize_json(
            value["memories"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMemoriesOutput:
    out: ListMemoriesOutput = {}  # type: ignore[typeddict-item]
    if "memories" in data:
        import aws_sdk_bedrock_agentcore_control.types.memory_summary_list

        out["memories"] = (
            aws_sdk_bedrock_agentcore_control.types.memory_summary_list.deserialize_json(
                data["memories"]
            )
        )
    else:
        raise DeserializationError("ListMemoriesOutput.memories required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
