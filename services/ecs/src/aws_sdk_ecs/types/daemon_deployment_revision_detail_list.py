"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDeploymentRevisionDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_deployment_revision_detail

DaemonDeploymentRevisionDetailList: TypeAlias = list[
    "aws_sdk_ecs.types.daemon_deployment_revision_detail.DaemonDeploymentRevisionDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonDeploymentRevisionDetailList) -> list:
    import aws_sdk_ecs.types.daemon_deployment_revision_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecs.types.daemon_deployment_revision_detail.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DaemonDeploymentRevisionDetailList:
    import aws_sdk_ecs.types.daemon_deployment_revision_detail

    out: DaemonDeploymentRevisionDetailList = []
    for item in data:
        out.append(
            aws_sdk_ecs.types.daemon_deployment_revision_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out
