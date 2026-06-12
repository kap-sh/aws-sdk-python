"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketBucketLifecycleConfigurationRulesTransitionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_transitions_details

AwsS3BucketBucketLifecycleConfigurationRulesTransitionsList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_transitions_details.AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsS3BucketBucketLifecycleConfigurationRulesTransitionsList,
) -> list:
    import aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_transitions_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_transitions_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsS3BucketBucketLifecycleConfigurationRulesTransitionsList:
    import aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_transitions_details

    out: AwsS3BucketBucketLifecycleConfigurationRulesTransitionsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_transitions_details.deserialize_json(
                item
            )
        )
    return out
