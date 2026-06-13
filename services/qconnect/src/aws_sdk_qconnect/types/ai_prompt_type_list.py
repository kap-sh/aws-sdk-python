"""Generated from Smithy shape ``com.amazonaws.qconnect#AIPromptTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_prompt_type

AIPromptTypeList: TypeAlias = list["aws_sdk_qconnect.types.ai_prompt_type.AIPromptType"]


# --- restJson1 ser/de ---
def serialize_json(value: AIPromptTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> AIPromptTypeList:
    return list(data)
