"""Generated from Smithy shape ``com.amazonaws.sagemaker#HumanTaskUiSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.human_task_ui_summary

HumanTaskUiSummaries: TypeAlias = list[
    "capo_sagemaker.types.human_task_ui_summary.HumanTaskUiSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HumanTaskUiSummaries) -> list:
    import capo_sagemaker.types.human_task_ui_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.human_task_ui_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> HumanTaskUiSummaries:
    import capo_sagemaker.types.human_task_ui_summary

    out: HumanTaskUiSummaries = []
    for item in data:
        out.append(
            capo_sagemaker.types.human_task_ui_summary.deserialize_aws_json_1_1(item)
        )
    return out
