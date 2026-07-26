"""Generated from Smithy shape ``com.amazonaws.bedrock#AdvancedPromptOptimizationJobStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of an advanced prompt optimization job.</p>"""
AdvancedPromptOptimizationJobStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
    "PartiallyCompleted",
    "Stopping",
    "Stopped",
    "Deleting",
]


# --- restJson1 ser/de ---
def serialize_json(value: AdvancedPromptOptimizationJobStatus) -> str:
    return value


def deserialize_json(data: str) -> AdvancedPromptOptimizationJobStatus:
    return cast(AdvancedPromptOptimizationJobStatus, data)
