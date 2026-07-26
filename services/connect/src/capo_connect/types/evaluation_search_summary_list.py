"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationSearchSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.evaluation_search_summary

EvaluationSearchSummaryList: TypeAlias = list[
    "capo_connect.types.evaluation_search_summary.EvaluationSearchSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationSearchSummaryList) -> list:
    import capo_connect.types.evaluation_search_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.evaluation_search_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> EvaluationSearchSummaryList:
    import capo_connect.types.evaluation_search_summary

    out: EvaluationSearchSummaryList = []
    for item in data:
        out.append(capo_connect.types.evaluation_search_summary.deserialize_json(item))
    return out
