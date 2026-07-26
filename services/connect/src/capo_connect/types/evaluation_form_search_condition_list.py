"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_search_criteria

EvaluationFormSearchConditionList: TypeAlias = list[
    "capo_connect.types.evaluation_form_search_criteria.EvaluationFormSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormSearchConditionList) -> list:
    import capo_connect.types.evaluation_form_search_criteria

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.evaluation_form_search_criteria.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EvaluationFormSearchConditionList:
    import capo_connect.types.evaluation_form_search_criteria

    out: EvaluationFormSearchConditionList = []
    for item in data:
        out.append(
            capo_connect.types.evaluation_form_search_criteria.deserialize_json(item)
        )
    return out
