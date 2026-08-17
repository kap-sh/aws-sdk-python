"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowTaskParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_task_parameters

MaintenanceWindowTaskParametersList: TypeAlias = list[
    "capo_ssm.types.maintenance_window_task_parameters.MaintenanceWindowTaskParameters"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowTaskParametersList) -> list:
    import capo_ssm.types.maintenance_window_task_parameters

    out: list = []
    for item in value:
        out.append(
            capo_ssm.types.maintenance_window_task_parameters.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MaintenanceWindowTaskParametersList:
    import capo_ssm.types.maintenance_window_task_parameters

    out: MaintenanceWindowTaskParametersList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ssm.types.maintenance_window_task_parameters.deserialize_aws_json_1_1(
                item
            )
        )
    return out
