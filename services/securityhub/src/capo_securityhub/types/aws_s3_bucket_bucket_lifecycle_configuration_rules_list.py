"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketBucketLifecycleConfigurationRulesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_details

AwsS3BucketBucketLifecycleConfigurationRulesList: TypeAlias = list[
    "capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_details.AwsS3BucketBucketLifecycleConfigurationRulesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketBucketLifecycleConfigurationRulesList) -> list:
    import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsS3BucketBucketLifecycleConfigurationRulesList:
    import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_details

    out: AwsS3BucketBucketLifecycleConfigurationRulesList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_details.deserialize_json(
                item
            )
        )
    return out
