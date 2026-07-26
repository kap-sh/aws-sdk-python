"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_noncurrent_version_transitions_details

AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsList: TypeAlias = list[
    "capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_noncurrent_version_transitions_details.AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsList,
) -> list:
    import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_noncurrent_version_transitions_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_noncurrent_version_transitions_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsList:
    import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_noncurrent_version_transitions_details

    out: AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_noncurrent_version_transitions_details.deserialize_json(
                item
            )
        )
    return out
