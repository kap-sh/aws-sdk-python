"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.maintenance_window_target

MaintenanceWindowTargetList: TypeAlias = list[
    "aws_sdk_ssm.types.maintenance_window_target.MaintenanceWindowTarget"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowTargetList) -> list:
    import aws_sdk_ssm.types.maintenance_window_target

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.maintenance_window_target.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MaintenanceWindowTargetList:
    import aws_sdk_ssm.types.maintenance_window_target

    out: MaintenanceWindowTargetList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.maintenance_window_target.deserialize_aws_json_1_1(item)
        )
    return out
