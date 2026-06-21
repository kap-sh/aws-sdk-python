"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDeploymentRollbackMonitorsStatus``."""

from typing import Literal, TypeAlias, cast

DaemonDeploymentRollbackMonitorsStatus: TypeAlias = Literal[
    "TRIGGERED",
    "MONITORING",
    "MONITORING_COMPLETE",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonDeploymentRollbackMonitorsStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DaemonDeploymentRollbackMonitorsStatus:
    return cast(DaemonDeploymentRollbackMonitorsStatus, data)
