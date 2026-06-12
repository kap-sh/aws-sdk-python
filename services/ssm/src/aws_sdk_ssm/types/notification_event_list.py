"""Generated from Smithy shape ``com.amazonaws.ssm#NotificationEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.notification_event

NotificationEventList: TypeAlias = list[
    "aws_sdk_ssm.types.notification_event.NotificationEvent"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotificationEventList) -> list:
    import aws_sdk_ssm.types.notification_event

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.notification_event.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> NotificationEventList:
    import aws_sdk_ssm.types.notification_event

    out: NotificationEventList = []
    for item in data:
        out.append(aws_sdk_ssm.types.notification_event.deserialize_aws_json_1_1(item))
    return out
