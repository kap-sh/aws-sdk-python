"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowsForTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_identity_for_target

MaintenanceWindowsForTargetList: TypeAlias = list[
    "capo_ssm.types.maintenance_window_identity_for_target.MaintenanceWindowIdentityForTarget"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowsForTargetList) -> list:
    import capo_ssm.types.maintenance_window_identity_for_target

    out: list = []
    for item in value:
        out.append(
            capo_ssm.types.maintenance_window_identity_for_target.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MaintenanceWindowsForTargetList:
    import capo_ssm.types.maintenance_window_identity_for_target

    out: MaintenanceWindowsForTargetList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ssm.types.maintenance_window_identity_for_target.deserialize_aws_json_1_1(
                item
            )
        )
    return out
