"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#OptimizePromptResponse``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.optimized_prompt_stream


class OptimizePromptResponse(TypedDict):
    optimized_prompt: "aws_sdk_bedrock_agent_runtime.types.optimized_prompt_stream.OptimizedPromptStream"
    """<p>The prompt after being optimized for the task.</p>"""
