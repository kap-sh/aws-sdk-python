"""Generated from Smithy shape ``com.amazonaws.sagemaker#NotebookInstanceLifecycleConfigSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.notebook_instance_lifecycle_config_summary

NotebookInstanceLifecycleConfigSummaryList: TypeAlias = list[
    "capo_sagemaker.types.notebook_instance_lifecycle_config_summary.NotebookInstanceLifecycleConfigSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotebookInstanceLifecycleConfigSummaryList) -> list:
    import capo_sagemaker.types.notebook_instance_lifecycle_config_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.notebook_instance_lifecycle_config_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> NotebookInstanceLifecycleConfigSummaryList:
    import capo_sagemaker.types.notebook_instance_lifecycle_config_summary

    out: NotebookInstanceLifecycleConfigSummaryList = []
    for item in data:
        out.append(
            capo_sagemaker.types.notebook_instance_lifecycle_config_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
