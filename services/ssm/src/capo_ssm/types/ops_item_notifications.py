"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemNotifications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.ops_item_notification

OpsItemNotifications: TypeAlias = list[
    "capo_ssm.types.ops_item_notification.OpsItemNotification"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemNotifications) -> list:
    import capo_ssm.types.ops_item_notification

    out: list = []
    for item in value:
        out.append(capo_ssm.types.ops_item_notification.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OpsItemNotifications:
    import capo_ssm.types.ops_item_notification

    out: OpsItemNotifications = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.ops_item_notification.deserialize_aws_json_1_1(item))
    return out
