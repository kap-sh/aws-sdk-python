"""Generated from Smithy shape ``com.amazonaws.sagemaker#MaintenanceStatus``."""

from typing import Literal, TypeAlias, cast

MaintenanceStatus: TypeAlias = Literal[
    "MaintenanceInProgress",
    "MaintenanceComplete",
    "MaintenanceFailed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MaintenanceStatus:
    return cast(MaintenanceStatus, data)
