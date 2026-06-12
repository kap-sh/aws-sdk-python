"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketNotificationConfigurationEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string

AwsS3BucketNotificationConfigurationEvents: TypeAlias = list[
    "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketNotificationConfigurationEvents) -> list:
    return list(value)


def deserialize_json(data: list) -> AwsS3BucketNotificationConfigurationEvents:
    return list(data)
