"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormSearchSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_search_summary

EvaluationFormSearchSummaryList: TypeAlias = list[
    "capo_connect.types.evaluation_form_search_summary.EvaluationFormSearchSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormSearchSummaryList) -> list:
    import capo_connect.types.evaluation_form_search_summary

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.evaluation_form_search_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EvaluationFormSearchSummaryList:
    import capo_connect.types.evaluation_form_search_summary

    out: EvaluationFormSearchSummaryList = []
    for item in data:
        out.append(
            capo_connect.types.evaluation_form_search_summary.deserialize_json(item)
        )
    return out
