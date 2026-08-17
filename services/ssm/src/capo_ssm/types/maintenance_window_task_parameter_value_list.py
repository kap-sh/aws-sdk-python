"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowTaskParameterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_task_parameter_value

MaintenanceWindowTaskParameterValueList: TypeAlias = list[
    "capo_ssm.types.maintenance_window_task_parameter_value.MaintenanceWindowTaskParameterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowTaskParameterValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> MaintenanceWindowTaskParameterValueList:
    return [item for item in data if item is not None]
