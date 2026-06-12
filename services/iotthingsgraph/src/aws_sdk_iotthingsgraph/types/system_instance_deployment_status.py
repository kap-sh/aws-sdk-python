"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SystemInstanceDeploymentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotthingsgraph.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_DEPLOYED",
        "BOOTSTRAP",
        "DEPLOY_IN_PROGRESS",
        "DEPLOYED_IN_TARGET",
        "UNDEPLOY_IN_PROGRESS",
        "FAILED",
        "PENDING_DELETE",
        "DELETED_IN_TARGET",
    )
)


def serialize_aws_json_1_1(value: SystemInstanceDeploymentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SystemInstanceDeploymentStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SystemInstanceDeploymentStatus value: {data!r}"
        )
    return cast(SystemInstanceDeploymentStatus, data)
