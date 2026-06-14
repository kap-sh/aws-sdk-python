"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessAgentCoreMemoryRetrievalConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.harness_agent_core_memory_retrieval_config

HarnessAgentCoreMemoryRetrievalConfigs: TypeAlias = dict[
    "str",
    "aws_sdk_bedrock_agentcore_control.types.harness_agent_core_memory_retrieval_config.HarnessAgentCoreMemoryRetrievalConfig",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: HarnessAgentCoreMemoryRetrievalConfigs) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_bedrock_agentcore_control.types.harness_agent_core_memory_retrieval_config

        out[key] = (
            aws_sdk_bedrock_agentcore_control.types.harness_agent_core_memory_retrieval_config.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> HarnessAgentCoreMemoryRetrievalConfigs:
    out: HarnessAgentCoreMemoryRetrievalConfigs = {}
    for key, value in data.items():
        import aws_sdk_bedrock_agentcore_control.types.harness_agent_core_memory_retrieval_config

        out[key] = (
            aws_sdk_bedrock_agentcore_control.types.harness_agent_core_memory_retrieval_config.deserialize_json(
                value
            )
        )
    return out
