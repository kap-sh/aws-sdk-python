"""Generated from Smithy shape ``com.amazonaws.ssmincidents#NotificationTargetSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.notification_target_item

NotificationTargetSet: TypeAlias = list[
    "aws_sdk_ssm_incidents.types.notification_target_item.NotificationTargetItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationTargetSet) -> list:
    import aws_sdk_ssm_incidents.types.notification_target_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm_incidents.types.notification_target_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NotificationTargetSet:
    import aws_sdk_ssm_incidents.types.notification_target_item

    out: NotificationTargetSet = []
    for item in data:
        out.append(
            aws_sdk_ssm_incidents.types.notification_target_item.deserialize_json(item)
        )
    return out
