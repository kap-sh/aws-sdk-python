"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceDeploymentRollbackMonitorsStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

ServiceDeploymentRollbackMonitorsStatus: TypeAlias = Literal[
    "TRIGGERED",
    "MONITORING",
    "MONITORING_COMPLETE",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRIGGERED",
        "MONITORING",
        "MONITORING_COMPLETE",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: ServiceDeploymentRollbackMonitorsStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceDeploymentRollbackMonitorsStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ServiceDeploymentRollbackMonitorsStatus value: {data!r}"
        )
    return cast(ServiceDeploymentRollbackMonitorsStatus, data)
