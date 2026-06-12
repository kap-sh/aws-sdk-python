"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowExecutionTaskIdentityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.maintenance_window_execution_task_identity

MaintenanceWindowExecutionTaskIdentityList: TypeAlias = list[
    "aws_sdk_ssm.types.maintenance_window_execution_task_identity.MaintenanceWindowExecutionTaskIdentity"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowExecutionTaskIdentityList) -> list:
    import aws_sdk_ssm.types.maintenance_window_execution_task_identity

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.maintenance_window_execution_task_identity.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MaintenanceWindowExecutionTaskIdentityList:
    import aws_sdk_ssm.types.maintenance_window_execution_task_identity

    out: MaintenanceWindowExecutionTaskIdentityList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.maintenance_window_execution_task_identity.deserialize_aws_json_1_1(
                item
            )
        )
    return out
