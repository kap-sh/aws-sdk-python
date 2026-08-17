"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDeploymentRevisionDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.daemon_deployment_revision_detail

DaemonDeploymentRevisionDetailList: TypeAlias = list[
    "capo_ecs.types.daemon_deployment_revision_detail.DaemonDeploymentRevisionDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonDeploymentRevisionDetailList) -> list:
    import capo_ecs.types.daemon_deployment_revision_detail

    out: list = []
    for item in value:
        out.append(
            capo_ecs.types.daemon_deployment_revision_detail.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DaemonDeploymentRevisionDetailList:
    import capo_ecs.types.daemon_deployment_revision_detail

    out: DaemonDeploymentRevisionDetailList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecs.types.daemon_deployment_revision_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out
