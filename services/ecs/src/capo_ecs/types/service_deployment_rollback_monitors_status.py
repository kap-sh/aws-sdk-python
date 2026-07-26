"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceDeploymentRollbackMonitorsStatus``."""

from typing import Literal, TypeAlias, cast

ServiceDeploymentRollbackMonitorsStatus: TypeAlias = Literal[
    "TRIGGERED",
    "MONITORING",
    "MONITORING_COMPLETE",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceDeploymentRollbackMonitorsStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceDeploymentRollbackMonitorsStatus:
    return cast(ServiceDeploymentRollbackMonitorsStatus, data)
