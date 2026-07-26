"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_operands_details

AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsList: TypeAlias = list[
    "capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_operands_details.AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsList,
) -> list:
    import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_operands_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_operands_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsList:
    import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_operands_details

    out: AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_operands_details.deserialize_json(
                item
            )
        )
    return out
