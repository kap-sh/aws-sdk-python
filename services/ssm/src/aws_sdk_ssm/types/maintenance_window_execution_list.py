"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowExecutionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.maintenance_window_execution

MaintenanceWindowExecutionList: TypeAlias = list[
    "aws_sdk_ssm.types.maintenance_window_execution.MaintenanceWindowExecution"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowExecutionList) -> list:
    import aws_sdk_ssm.types.maintenance_window_execution

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.maintenance_window_execution.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MaintenanceWindowExecutionList:
    import aws_sdk_ssm.types.maintenance_window_execution

    out: MaintenanceWindowExecutionList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.maintenance_window_execution.deserialize_aws_json_1_1(
                item
            )
        )
    return out
