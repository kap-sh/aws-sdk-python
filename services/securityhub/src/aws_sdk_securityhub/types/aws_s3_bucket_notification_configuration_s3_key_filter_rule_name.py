"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketNotificationConfigurationS3KeyFilterRuleName``."""

from typing import Literal, TypeAlias, cast

AwsS3BucketNotificationConfigurationS3KeyFilterRuleName: TypeAlias = Literal[
    "Prefix",
    "Suffix",
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsS3BucketNotificationConfigurationS3KeyFilterRuleName,
) -> str:
    return value


def deserialize_json(
    data: str,
) -> AwsS3BucketNotificationConfigurationS3KeyFilterRuleName:
    return cast(AwsS3BucketNotificationConfigurationS3KeyFilterRuleName, data)
