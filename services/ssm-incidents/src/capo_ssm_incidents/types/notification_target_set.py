"""Generated from Smithy shape ``com.amazonaws.ssmincidents#NotificationTargetSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_incidents.types.notification_target_item

NotificationTargetSet: TypeAlias = list[
    "capo_ssm_incidents.types.notification_target_item.NotificationTargetItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationTargetSet) -> list:
    import capo_ssm_incidents.types.notification_target_item

    out: list = []
    for item in value:
        out.append(
            capo_ssm_incidents.types.notification_target_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NotificationTargetSet:
    import capo_ssm_incidents.types.notification_target_item

    out: NotificationTargetSet = []
    for item in data:
        out.append(
            capo_ssm_incidents.types.notification_target_item.deserialize_json(item)
        )
    return out
