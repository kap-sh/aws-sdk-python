"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_operands_list
    import aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_tag_details
    import aws_sdk_securityhub.types.non_empty_string


class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetails(TypedDict):
    operands: NotRequired[
        "aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_operands_list.AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsList"
    ]
    """<p>The values to use for the filter.</p>"""
    prefix: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A prefix filter.</p>"""
    tag: NotRequired[
        "aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_tag_details.AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetails"
    ]
    """<p>A tag filter.</p>"""
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Whether to use <code>AND</code> or <code>OR</code> to join the operands. Valid values are <code>LifecycleAndOperator</code> or <code>LifecycleOrOperator</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetails,
) -> dict:
    out: dict = {}
    if "operands" in value:
        import aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_operands_list

        out["Operands"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_operands_list.serialize_json(
                value["operands"]
            )
        )
    if "prefix" in value:
        out["Prefix"] = value["prefix"]
    if "tag" in value:
        import aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_tag_details

        out["Tag"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_tag_details.serialize_json(
                value["tag"]
            )
        )
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(
    data: dict,
) -> AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetails:
    out: AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetails = {}  # type: ignore[typeddict-item]
    if "Operands" in data:
        import aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_operands_list

        out["operands"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_operands_list.deserialize_json(
                data["Operands"]
            )
        )
    if "Prefix" in data:
        out["prefix"] = data["Prefix"]
    if "Tag" in data:
        import aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_tag_details

        out["tag"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_tag_details.deserialize_json(
                data["Tag"]
            )
        )
    if "Type" in data:
        out["type"] = data["Type"]
    return out
