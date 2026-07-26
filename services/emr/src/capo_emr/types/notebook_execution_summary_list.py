"""Generated from Smithy shape ``com.amazonaws.emr#NotebookExecutionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.notebook_execution_summary

NotebookExecutionSummaryList: TypeAlias = list[
    "capo_emr.types.notebook_execution_summary.NotebookExecutionSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotebookExecutionSummaryList) -> list:
    import capo_emr.types.notebook_execution_summary

    out: list = []
    for item in value:
        out.append(
            capo_emr.types.notebook_execution_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> NotebookExecutionSummaryList:
    import capo_emr.types.notebook_execution_summary

    out: NotebookExecutionSummaryList = []
    for item in data:
        out.append(
            capo_emr.types.notebook_execution_summary.deserialize_aws_json_1_1(item)
        )
    return out
