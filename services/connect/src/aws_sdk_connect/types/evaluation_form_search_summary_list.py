"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormSearchSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_form_search_summary

EvaluationFormSearchSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.evaluation_form_search_summary.EvaluationFormSearchSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormSearchSummaryList) -> list:
    import aws_sdk_connect.types.evaluation_form_search_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.evaluation_form_search_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EvaluationFormSearchSummaryList:
    import aws_sdk_connect.types.evaluation_form_search_summary

    out: EvaluationFormSearchSummaryList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.evaluation_form_search_summary.deserialize_json(item)
        )
    return out
