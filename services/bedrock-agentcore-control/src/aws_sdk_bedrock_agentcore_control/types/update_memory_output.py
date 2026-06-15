"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateMemoryOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.memory


class UpdateMemoryOutput(TypedDict):
    memory: NotRequired["aws_sdk_bedrock_agentcore_control.types.memory.Memory"]
    """<p>The updated AgentCore Memory resource details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMemoryOutput) -> dict:
    out: dict = {}
    if "memory" in value:
        import aws_sdk_bedrock_agentcore_control.types.memory

        out["memory"] = aws_sdk_bedrock_agentcore_control.types.memory.serialize_json(
            value["memory"]
        )
    return out


def deserialize_json(data: dict) -> UpdateMemoryOutput:
    out: UpdateMemoryOutput = {}  # type: ignore[typeddict-item]
    if "memory" in data:
        import aws_sdk_bedrock_agentcore_control.types.memory

        out["memory"] = aws_sdk_bedrock_agentcore_control.types.memory.deserialize_json(
            data["memory"]
        )
    return out
