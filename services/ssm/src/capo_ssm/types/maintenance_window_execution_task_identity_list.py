"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowExecutionTaskIdentityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_execution_task_identity

MaintenanceWindowExecutionTaskIdentityList: TypeAlias = list[
    "capo_ssm.types.maintenance_window_execution_task_identity.MaintenanceWindowExecutionTaskIdentity"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowExecutionTaskIdentityList) -> list:
    import capo_ssm.types.maintenance_window_execution_task_identity

    out: list = []
    for item in value:
        out.append(
            capo_ssm.types.maintenance_window_execution_task_identity.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MaintenanceWindowExecutionTaskIdentityList:
    import capo_ssm.types.maintenance_window_execution_task_identity

    out: MaintenanceWindowExecutionTaskIdentityList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ssm.types.maintenance_window_execution_task_identity.deserialize_aws_json_1_1(
                item
            )
        )
    return out
