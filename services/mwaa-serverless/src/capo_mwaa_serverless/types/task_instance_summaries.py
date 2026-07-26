"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#TaskInstanceSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.task_instance_summary

TaskInstanceSummaries: TypeAlias = list[
    "capo_mwaa_serverless.types.task_instance_summary.TaskInstanceSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaskInstanceSummaries) -> list:
    import capo_mwaa_serverless.types.task_instance_summary

    out: list = []
    for item in value:
        out.append(
            capo_mwaa_serverless.types.task_instance_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> TaskInstanceSummaries:
    import capo_mwaa_serverless.types.task_instance_summary

    out: TaskInstanceSummaries = []
    for item in data:
        out.append(
            capo_mwaa_serverless.types.task_instance_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
