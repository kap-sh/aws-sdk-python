"""Generated from Smithy shape ``com.amazonaws.quicksight#StarterPromptList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.starter_prompt

StarterPromptList: TypeAlias = list[
    "aws_sdk_quicksight.types.starter_prompt.StarterPrompt"
]


# --- restJson1 ser/de ---
def serialize_json(value: StarterPromptList) -> list:
    return list(value)


def deserialize_json(data: list) -> StarterPromptList:
    return list(data)
