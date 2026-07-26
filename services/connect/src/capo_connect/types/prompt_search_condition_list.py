"""Generated from Smithy shape ``com.amazonaws.connect#PromptSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.prompt_search_criteria

PromptSearchConditionList: TypeAlias = list[
    "capo_connect.types.prompt_search_criteria.PromptSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: PromptSearchConditionList) -> list:
    import capo_connect.types.prompt_search_criteria

    out: list = []
    for item in value:
        out.append(capo_connect.types.prompt_search_criteria.serialize_json(item))
    return out


def deserialize_json(data: list) -> PromptSearchConditionList:
    import capo_connect.types.prompt_search_criteria

    out: PromptSearchConditionList = []
    for item in data:
        out.append(capo_connect.types.prompt_search_criteria.deserialize_json(item))
    return out
