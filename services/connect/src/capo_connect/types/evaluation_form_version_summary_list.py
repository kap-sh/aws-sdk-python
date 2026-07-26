"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormVersionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_version_summary

EvaluationFormVersionSummaryList: TypeAlias = list[
    "capo_connect.types.evaluation_form_version_summary.EvaluationFormVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormVersionSummaryList) -> list:
    import capo_connect.types.evaluation_form_version_summary

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.evaluation_form_version_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EvaluationFormVersionSummaryList:
    import capo_connect.types.evaluation_form_version_summary

    out: EvaluationFormVersionSummaryList = []
    for item in data:
        out.append(
            capo_connect.types.evaluation_form_version_summary.deserialize_json(item)
        )
    return out
