"""Generated from Smithy shape ``com.amazonaws.servicecatalog#NotificationArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.notification_arn

NotificationArns: TypeAlias = list[
    "aws_sdk_service_catalog.types.notification_arn.NotificationArn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotificationArns) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> NotificationArns:
    return list(data)
