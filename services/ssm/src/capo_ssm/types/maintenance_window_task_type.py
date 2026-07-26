"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowTaskType``."""

from typing import Literal, TypeAlias, cast

MaintenanceWindowTaskType: TypeAlias = Literal[
    "RUN_COMMAND",
    "AUTOMATION",
    "STEP_FUNCTIONS",
    "LAMBDA",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowTaskType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MaintenanceWindowTaskType:
    return cast(MaintenanceWindowTaskType, data)
