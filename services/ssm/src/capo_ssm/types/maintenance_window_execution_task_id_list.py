"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowExecutionTaskIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_execution_task_id

MaintenanceWindowExecutionTaskIdList: TypeAlias = list[
    "capo_ssm.types.maintenance_window_execution_task_id.MaintenanceWindowExecutionTaskId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowExecutionTaskIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> MaintenanceWindowExecutionTaskIdList:
    return [item for item in data if item is not None]
