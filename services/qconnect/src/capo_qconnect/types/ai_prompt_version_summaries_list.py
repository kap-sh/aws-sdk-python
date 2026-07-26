"""Generated from Smithy shape ``com.amazonaws.qconnect#AIPromptVersionSummariesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.ai_prompt_version_summary

AIPromptVersionSummariesList: TypeAlias = list[
    "capo_qconnect.types.ai_prompt_version_summary.AIPromptVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AIPromptVersionSummariesList) -> list:
    import capo_qconnect.types.ai_prompt_version_summary

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.ai_prompt_version_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AIPromptVersionSummariesList:
    import capo_qconnect.types.ai_prompt_version_summary

    out: AIPromptVersionSummariesList = []
    for item in data:
        out.append(capo_qconnect.types.ai_prompt_version_summary.deserialize_json(item))
    return out
