"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_search_criteria

EvaluationSearchConditionList: TypeAlias = list[
    "aws_sdk_connect.types.evaluation_search_criteria.EvaluationSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationSearchConditionList) -> list:
    import aws_sdk_connect.types.evaluation_search_criteria

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.evaluation_search_criteria.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EvaluationSearchConditionList:
    import aws_sdk_connect.types.evaluation_search_criteria

    out: EvaluationSearchConditionList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.evaluation_search_criteria.deserialize_json(item)
        )
    return out
