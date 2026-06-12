"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_form_summary

EvaluationFormSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.evaluation_form_summary.EvaluationFormSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormSummaryList) -> list:
    import aws_sdk_connect.types.evaluation_form_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.evaluation_form_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> EvaluationFormSummaryList:
    import aws_sdk_connect.types.evaluation_form_summary

    out: EvaluationFormSummaryList = []
    for item in data:
        out.append(aws_sdk_connect.types.evaluation_form_summary.deserialize_json(item))
    return out
