"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_filter_value

MaintenanceWindowFilterValues: TypeAlias = list[
    "capo_ssm.types.maintenance_window_filter_value.MaintenanceWindowFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> MaintenanceWindowFilterValues:
    return list(data)
