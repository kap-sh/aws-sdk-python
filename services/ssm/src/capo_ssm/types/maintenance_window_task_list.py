"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowTaskList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_task

MaintenanceWindowTaskList: TypeAlias = list[
    "capo_ssm.types.maintenance_window_task.MaintenanceWindowTask"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowTaskList) -> list:
    import capo_ssm.types.maintenance_window_task

    out: list = []
    for item in value:
        out.append(capo_ssm.types.maintenance_window_task.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MaintenanceWindowTaskList:
    import capo_ssm.types.maintenance_window_task

    out: MaintenanceWindowTaskList = []
    for item in data:
        out.append(
            capo_ssm.types.maintenance_window_task.deserialize_aws_json_1_1(item)
        )
    return out
