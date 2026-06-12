"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowsForTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.maintenance_window_identity_for_target

MaintenanceWindowsForTargetList: TypeAlias = list[
    "aws_sdk_ssm.types.maintenance_window_identity_for_target.MaintenanceWindowIdentityForTarget"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowsForTargetList) -> list:
    import aws_sdk_ssm.types.maintenance_window_identity_for_target

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.maintenance_window_identity_for_target.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MaintenanceWindowsForTargetList:
    import aws_sdk_ssm.types.maintenance_window_identity_for_target

    out: MaintenanceWindowsForTargetList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.maintenance_window_identity_for_target.deserialize_aws_json_1_1(
                item
            )
        )
    return out
