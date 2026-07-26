"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#OptimizePromptResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.optimized_prompt_stream


class OptimizePromptResponse(TypedDict, closed=True):
    optimized_prompt: (
        "capo_bedrock_agent_runtime.types.optimized_prompt_stream.OptimizedPromptStream"
    )
    """<p>The prompt after being optimized for the task.</p>"""
