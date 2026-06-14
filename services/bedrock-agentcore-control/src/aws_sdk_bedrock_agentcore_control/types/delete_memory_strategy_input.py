"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteMemoryStrategyInput``."""

from typing import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError


class DeleteMemoryStrategyInput(TypedDict):
    memory_strategy_id: "str"
    """<p>The unique identifier of the memory strategy to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMemoryStrategyInput) -> dict:
    out: dict = {}
    out["memoryStrategyId"] = value["memory_strategy_id"]
    return out


def deserialize_json(data: dict) -> DeleteMemoryStrategyInput:
    out: DeleteMemoryStrategyInput = {}  # type: ignore[typeddict-item]
    if "memoryStrategyId" in data:
        out["memory_strategy_id"] = data["memoryStrategyId"]
    else:
        raise DeserializationError(
            "DeleteMemoryStrategyInput.memory_strategy_id required"
        )
    return out
