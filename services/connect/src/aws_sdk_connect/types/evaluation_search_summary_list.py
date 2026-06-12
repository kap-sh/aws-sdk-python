"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationSearchSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_search_summary

EvaluationSearchSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.evaluation_search_summary.EvaluationSearchSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationSearchSummaryList) -> list:
    import aws_sdk_connect.types.evaluation_search_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.evaluation_search_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> EvaluationSearchSummaryList:
    import aws_sdk_connect.types.evaluation_search_summary

    out: EvaluationSearchSummaryList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.evaluation_search_summary.deserialize_json(item)
        )
    return out
