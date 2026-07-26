"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_summary

EvaluationFormSummaryList: TypeAlias = list[
    "capo_connect.types.evaluation_form_summary.EvaluationFormSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormSummaryList) -> list:
    import capo_connect.types.evaluation_form_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.evaluation_form_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> EvaluationFormSummaryList:
    import capo_connect.types.evaluation_form_summary

    out: EvaluationFormSummaryList = []
    for item in data:
        out.append(capo_connect.types.evaluation_form_summary.deserialize_json(item))
    return out
