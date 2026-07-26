"""Generated from Smithy shape ``com.amazonaws.connect#PromptSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.prompt_summary

PromptSummaryList: TypeAlias = list["capo_connect.types.prompt_summary.PromptSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: PromptSummaryList) -> list:
    import capo_connect.types.prompt_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.prompt_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> PromptSummaryList:
    import capo_connect.types.prompt_summary

    out: PromptSummaryList = []
    for item in data:
        out.append(capo_connect.types.prompt_summary.deserialize_json(item))
    return out
