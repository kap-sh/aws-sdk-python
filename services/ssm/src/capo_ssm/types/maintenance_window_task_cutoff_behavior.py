"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowTaskCutoffBehavior``."""

from typing import Literal, TypeAlias, cast

MaintenanceWindowTaskCutoffBehavior: TypeAlias = Literal[
    "CONTINUE_TASK",
    "CANCEL_TASK",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowTaskCutoffBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MaintenanceWindowTaskCutoffBehavior:
    return cast(MaintenanceWindowTaskCutoffBehavior, data)
