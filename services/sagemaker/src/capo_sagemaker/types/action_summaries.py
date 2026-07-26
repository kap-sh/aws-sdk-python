"""Generated from Smithy shape ``com.amazonaws.sagemaker#ActionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.action_summary

ActionSummaries: TypeAlias = list["capo_sagemaker.types.action_summary.ActionSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionSummaries) -> list:
    import capo_sagemaker.types.action_summary

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.action_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ActionSummaries:
    import capo_sagemaker.types.action_summary

    out: ActionSummaries = []
    for item in data:
        out.append(capo_sagemaker.types.action_summary.deserialize_aws_json_1_1(item))
    return out
