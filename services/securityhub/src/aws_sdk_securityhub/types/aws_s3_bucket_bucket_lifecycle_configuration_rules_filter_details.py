"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketBucketLifecycleConfigurationRulesFilterDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_details


class AwsS3BucketBucketLifecycleConfigurationRulesFilterDetails(TypedDict):
    predicate: NotRequired[
        "aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_details.AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetails"
    ]
    """<p>The configuration for the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsS3BucketBucketLifecycleConfigurationRulesFilterDetails,
) -> dict:
    out: dict = {}
    if "predicate" in value:
        import aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_details

        out["Predicate"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_details.serialize_json(
                value["predicate"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> AwsS3BucketBucketLifecycleConfigurationRulesFilterDetails:
    out: AwsS3BucketBucketLifecycleConfigurationRulesFilterDetails = {}  # type: ignore[typeddict-item]
    if "Predicate" in data:
        import aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_details

        out["predicate"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_details.deserialize_json(
                data["Predicate"]
            )
        )
    return out
