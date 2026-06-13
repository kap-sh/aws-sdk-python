"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#OptimizedPromptEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.optimized_prompt


class OptimizedPromptEvent(TypedDict):
    optimized_prompt: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.optimized_prompt.OptimizedPrompt"
    ]
    """<p>Contains information about the optimized prompt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OptimizedPromptEvent) -> dict:
    out: dict = {}
    if "optimized_prompt" in value:
        import aws_sdk_bedrock_agent_runtime.types.optimized_prompt

        out["optimizedPrompt"] = (
            aws_sdk_bedrock_agent_runtime.types.optimized_prompt.serialize_json(
                value["optimized_prompt"]
            )
        )
    return out


def deserialize_json(data: dict) -> OptimizedPromptEvent:
    out: OptimizedPromptEvent = {}  # type: ignore[typeddict-item]
    if "optimizedPrompt" in data:
        import aws_sdk_bedrock_agent_runtime.types.optimized_prompt

        out["optimized_prompt"] = (
            aws_sdk_bedrock_agent_runtime.types.optimized_prompt.deserialize_json(
                data["optimizedPrompt"]
            )
        )
    return out
