"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.evaluation_search_criteria

EvaluationSearchConditionList: TypeAlias = list[
    "capo_connect.types.evaluation_search_criteria.EvaluationSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationSearchConditionList) -> list:
    import capo_connect.types.evaluation_search_criteria

    out: list = []
    for item in value:
        out.append(capo_connect.types.evaluation_search_criteria.serialize_json(item))
    return out


def deserialize_json(data: list) -> EvaluationSearchConditionList:
    import capo_connect.types.evaluation_search_criteria

    out: EvaluationSearchConditionList = []
    for item in data:
        out.append(capo_connect.types.evaluation_search_criteria.deserialize_json(item))
    return out
