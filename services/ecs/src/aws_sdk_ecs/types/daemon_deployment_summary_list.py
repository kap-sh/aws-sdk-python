"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDeploymentSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_deployment_summary

DaemonDeploymentSummaryList: TypeAlias = list[
    "aws_sdk_ecs.types.daemon_deployment_summary.DaemonDeploymentSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonDeploymentSummaryList) -> list:
    import aws_sdk_ecs.types.daemon_deployment_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecs.types.daemon_deployment_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DaemonDeploymentSummaryList:
    import aws_sdk_ecs.types.daemon_deployment_summary

    out: DaemonDeploymentSummaryList = []
    for item in data:
        out.append(
            aws_sdk_ecs.types.daemon_deployment_summary.deserialize_aws_json_1_1(item)
        )
    return out
