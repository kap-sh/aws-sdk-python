"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetMemoryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.memory


class GetMemoryOutput(TypedDict, closed=True):
    memory: "aws_sdk_bedrock_agentcore_control.types.memory.Memory"
    """<p>The retrieved AgentCore Memory resource details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMemoryOutput) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.memory

    out["memory"] = aws_sdk_bedrock_agentcore_control.types.memory.serialize_json(
        value["memory"]
    )
    return out


def deserialize_json(data: dict) -> GetMemoryOutput:
    out: GetMemoryOutput = {}  # type: ignore[typeddict-item]
    if "memory" in data:
        import aws_sdk_bedrock_agentcore_control.types.memory

        out["memory"] = aws_sdk_bedrock_agentcore_control.types.memory.deserialize_json(
            data["memory"]
        )
    else:
        raise DeserializationError("GetMemoryOutput.memory required")
    return out
