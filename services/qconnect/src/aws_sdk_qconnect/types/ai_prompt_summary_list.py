"""Generated from Smithy shape ``com.amazonaws.qconnect#AIPromptSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_prompt_summary

AIPromptSummaryList: TypeAlias = list[
    "aws_sdk_qconnect.types.ai_prompt_summary.AIPromptSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AIPromptSummaryList) -> list:
    import aws_sdk_qconnect.types.ai_prompt_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_qconnect.types.ai_prompt_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AIPromptSummaryList:
    import aws_sdk_qconnect.types.ai_prompt_summary

    out: AIPromptSummaryList = []
    for item in data:
        out.append(aws_sdk_qconnect.types.ai_prompt_summary.deserialize_json(item))
    return out
