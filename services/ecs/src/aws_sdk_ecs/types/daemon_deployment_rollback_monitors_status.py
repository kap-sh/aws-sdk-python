"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDeploymentRollbackMonitorsStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

DaemonDeploymentRollbackMonitorsStatus: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: DaemonDeploymentRollbackMonitorsStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DaemonDeploymentRollbackMonitorsStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DaemonDeploymentRollbackMonitorsStatus value: {data!r}"
        )
    return cast(DaemonDeploymentRollbackMonitorsStatus, data)
