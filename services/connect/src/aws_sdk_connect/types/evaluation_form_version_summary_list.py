"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormVersionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_form_version_summary

EvaluationFormVersionSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.evaluation_form_version_summary.EvaluationFormVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormVersionSummaryList) -> list:
    import aws_sdk_connect.types.evaluation_form_version_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.evaluation_form_version_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EvaluationFormVersionSummaryList:
    import aws_sdk_connect.types.evaluation_form_version_summary

    out: EvaluationFormVersionSummaryList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.evaluation_form_version_summary.deserialize_json(item)
        )
    return out
