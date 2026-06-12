"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.maintenance_window_filter

MaintenanceWindowFilterList: TypeAlias = list[
    "aws_sdk_ssm.types.maintenance_window_filter.MaintenanceWindowFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowFilterList) -> list:
    import aws_sdk_ssm.types.maintenance_window_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.maintenance_window_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MaintenanceWindowFilterList:
    import aws_sdk_ssm.types.maintenance_window_filter

    out: MaintenanceWindowFilterList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.maintenance_window_filter.deserialize_aws_json_1_1(item)
        )
    return out
