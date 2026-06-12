"""Generated from Smithy shape ``com.amazonaws.sagemaker#HumanTaskUiSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.human_task_ui_summary

HumanTaskUiSummaries: TypeAlias = list[
    "aws_sdk_sagemaker.types.human_task_ui_summary.HumanTaskUiSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HumanTaskUiSummaries) -> list:
    import aws_sdk_sagemaker.types.human_task_ui_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.human_task_ui_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> HumanTaskUiSummaries:
    import aws_sdk_sagemaker.types.human_task_ui_summary

    out: HumanTaskUiSummaries = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.human_task_ui_summary.deserialize_aws_json_1_1(item)
        )
    return out
