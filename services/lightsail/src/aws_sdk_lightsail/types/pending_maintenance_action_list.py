"""Generated from Smithy shape ``com.amazonaws.lightsail#PendingMaintenanceActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.pending_maintenance_action

PendingMaintenanceActionList: TypeAlias = list[
    "aws_sdk_lightsail.types.pending_maintenance_action.PendingMaintenanceAction"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PendingMaintenanceActionList) -> list:
    import aws_sdk_lightsail.types.pending_maintenance_action

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lightsail.types.pending_maintenance_action.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PendingMaintenanceActionList:
    import aws_sdk_lightsail.types.pending_maintenance_action

    out: PendingMaintenanceActionList = []
    for item in data:
        out.append(
            aws_sdk_lightsail.types.pending_maintenance_action.deserialize_aws_json_1_1(
                item
            )
        )
    return out
