"""Generated from Smithy shape ``com.amazonaws.sagemaker#NotebookInstanceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.notebook_instance_summary

NotebookInstanceSummaryList: TypeAlias = list[
    "capo_sagemaker.types.notebook_instance_summary.NotebookInstanceSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotebookInstanceSummaryList) -> list:
    import capo_sagemaker.types.notebook_instance_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.notebook_instance_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> NotebookInstanceSummaryList:
    import capo_sagemaker.types.notebook_instance_summary

    out: NotebookInstanceSummaryList = []
    for item in data:
        out.append(
            capo_sagemaker.types.notebook_instance_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
