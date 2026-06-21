"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SystemInstanceDeploymentStatus``."""

from typing import Literal, TypeAlias, cast

SystemInstanceDeploymentStatus: TypeAlias = Literal[
    "NOT_DEPLOYED",
    "BOOTSTRAP",
    "DEPLOY_IN_PROGRESS",
    "DEPLOYED_IN_TARGET",
    "UNDEPLOY_IN_PROGRESS",
    "FAILED",
    "PENDING_DELETE",
    "DELETED_IN_TARGET",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SystemInstanceDeploymentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SystemInstanceDeploymentStatus:
    return cast(SystemInstanceDeploymentStatus, data)
