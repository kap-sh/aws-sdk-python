"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_summary

EvaluationSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.evaluation_summary.EvaluationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationSummaryList) -> list:
    import aws_sdk_connect.types.evaluation_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.evaluation_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> EvaluationSummaryList:
    import aws_sdk_connect.types.evaluation_summary

    out: EvaluationSummaryList = []
    for item in data:
        out.append(aws_sdk_connect.types.evaluation_summary.deserialize_json(item))
    return out
