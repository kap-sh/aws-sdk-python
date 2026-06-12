"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowExecutionTaskIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.maintenance_window_execution_task_id

MaintenanceWindowExecutionTaskIdList: TypeAlias = list[
    "aws_sdk_ssm.types.maintenance_window_execution_task_id.MaintenanceWindowExecutionTaskId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowExecutionTaskIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> MaintenanceWindowExecutionTaskIdList:
    return list(data)
