"""Generated from Smithy shape ``com.amazonaws.qconnect#AIPromptVersionSummariesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_prompt_version_summary

AIPromptVersionSummariesList: TypeAlias = list[
    "aws_sdk_qconnect.types.ai_prompt_version_summary.AIPromptVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AIPromptVersionSummariesList) -> list:
    import aws_sdk_qconnect.types.ai_prompt_version_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_qconnect.types.ai_prompt_version_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AIPromptVersionSummariesList:
    import aws_sdk_qconnect.types.ai_prompt_version_summary

    out: AIPromptVersionSummariesList = []
    for item in data:
        out.append(
            aws_sdk_qconnect.types.ai_prompt_version_summary.deserialize_json(item)
        )
    return out
