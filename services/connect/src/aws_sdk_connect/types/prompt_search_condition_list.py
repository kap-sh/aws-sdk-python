"""Generated from Smithy shape ``com.amazonaws.connect#PromptSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.prompt_search_criteria

PromptSearchConditionList: TypeAlias = list[
    "aws_sdk_connect.types.prompt_search_criteria.PromptSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: PromptSearchConditionList) -> list:
    import aws_sdk_connect.types.prompt_search_criteria

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.prompt_search_criteria.serialize_json(item))
    return out


def deserialize_json(data: list) -> PromptSearchConditionList:
    import aws_sdk_connect.types.prompt_search_criteria

    out: PromptSearchConditionList = []
    for item in data:
        out.append(aws_sdk_connect.types.prompt_search_criteria.deserialize_json(item))
    return out
