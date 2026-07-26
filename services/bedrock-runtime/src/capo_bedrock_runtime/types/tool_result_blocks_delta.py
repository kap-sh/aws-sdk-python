"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ToolResultBlocksDelta``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.tool_result_block_delta

ToolResultBlocksDelta: TypeAlias = list[
    "capo_bedrock_runtime.types.tool_result_block_delta.ToolResultBlockDelta"
]


# --- restJson1 ser/de ---
def serialize_json(value: ToolResultBlocksDelta) -> list:
    import capo_bedrock_runtime.types.tool_result_block_delta

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_runtime.types.tool_result_block_delta.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ToolResultBlocksDelta:
    import capo_bedrock_runtime.types.tool_result_block_delta

    out: ToolResultBlocksDelta = []
    for item in data:
        out.append(
            capo_bedrock_runtime.types.tool_result_block_delta.deserialize_json(item)
        )
    return out
