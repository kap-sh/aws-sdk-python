"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketNotificationConfigurationS3KeyFilterRuleName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

AwsS3BucketNotificationConfigurationS3KeyFilterRuleName: TypeAlias = Literal[
    "Prefix",
    "Suffix",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Prefix",
        "Suffix",
    )
)


def serialize_json(
    value: AwsS3BucketNotificationConfigurationS3KeyFilterRuleName,
) -> str:
    return value


def deserialize_json(
    data: str,
) -> AwsS3BucketNotificationConfigurationS3KeyFilterRuleName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AwsS3BucketNotificationConfigurationS3KeyFilterRuleName value: {data!r}"
        )
    return cast(AwsS3BucketNotificationConfigurationS3KeyFilterRuleName, data)
