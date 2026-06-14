"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessTools``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.harness_tool

HarnessTools: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.harness_tool.HarnessTool"
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessTools) -> list:
    import aws_sdk_bedrock_agentcore_control.types.harness_tool

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.harness_tool.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> HarnessTools:
    import aws_sdk_bedrock_agentcore_control.types.harness_tool

    out: HarnessTools = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.harness_tool.deserialize_json(item)
        )
    return out
