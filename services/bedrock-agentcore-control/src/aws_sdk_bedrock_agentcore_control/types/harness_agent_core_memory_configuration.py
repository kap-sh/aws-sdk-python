"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessAgentCoreMemoryConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.harness_agent_core_memory_retrieval_configs
    import aws_sdk_bedrock_agentcore_control.types.memory_arn

class HarnessAgentCoreMemoryConfiguration(TypedDict):
    arn: "aws_sdk_bedrock_agentcore_control.types.memory_arn.MemoryArn"
    """<p>The ARN of the AgentCore Memory resource.</p>"""
    actor_id: NotRequired["str"]
    """<p>The actor ID for memory operations.</p>"""
    messages_count: NotRequired["int"]
    """<p>The number of messages to retrieve from memory.</p>"""
    retrieval_config: NotRequired["aws_sdk_bedrock_agentcore_control.types.harness_agent_core_memory_retrieval_configs.HarnessAgentCoreMemoryRetrievalConfigs"]
    """<p>The retrieval configuration for long-term memory, mapping namespace path templates to retrieval settings.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: HarnessAgentCoreMemoryConfiguration) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "actor_id" in value:
        out["actorId"] = value["actor_id"]
    if "messages_count" in value:
        out["messagesCount"] = value["messages_count"]
    if "retrieval_config" in value:
        import aws_sdk_bedrock_agentcore_control.types.harness_agent_core_memory_retrieval_configs
        out["retrievalConfig"] = aws_sdk_bedrock_agentcore_control.types.harness_agent_core_memory_retrieval_configs.serialize_json(value["retrieval_config"])
    return out


def deserialize_json(data: dict) -> HarnessAgentCoreMemoryConfiguration:
    out: HarnessAgentCoreMemoryConfiguration = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("HarnessAgentCoreMemoryConfiguration.arn required")
    if "actorId" in data:
        out["actor_id"] = data["actorId"]
    if "messagesCount" in data:
        out["messages_count"] = data["messagesCount"]
    if "retrievalConfig" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_agent_core_memory_retrieval_configs
        out["retrieval_config"] = aws_sdk_bedrock_agentcore_control.types.harness_agent_core_memory_retrieval_configs.deserialize_json(data["retrievalConfig"])
    return out