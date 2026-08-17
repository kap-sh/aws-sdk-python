"""Generated from Smithy shape ``com.amazonaws.ssm#NotificationEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.notification_event

NotificationEventList: TypeAlias = list[
    "capo_ssm.types.notification_event.NotificationEvent"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotificationEventList) -> list:
    import capo_ssm.types.notification_event

    out: list = []
    for item in value:
        out.append(capo_ssm.types.notification_event.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> NotificationEventList:
    import capo_ssm.types.notification_event

    out: NotificationEventList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.notification_event.deserialize_aws_json_1_1(item))
    return out
