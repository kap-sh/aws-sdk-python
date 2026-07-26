"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketBucketLifecycleConfigurationRulesFilterDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_details


class AwsS3BucketBucketLifecycleConfigurationRulesFilterDetails(TypedDict, closed=True):
    predicate: NotRequired[
        "capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_details.AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetails"
    ]
    """<p>The configuration for the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsS3BucketBucketLifecycleConfigurationRulesFilterDetails,
) -> dict:
    out: dict = {}
    if "predicate" in value:
        import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_details

        out["Predicate"] = (
            capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_details.serialize_json(
                value["predicate"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> AwsS3BucketBucketLifecycleConfigurationRulesFilterDetails:
    out: AwsS3BucketBucketLifecycleConfigurationRulesFilterDetails = {}  # type: ignore[typeddict-item]
    if "Predicate" in data:
        import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_details

        out["predicate"] = (
            capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_predicate_details.deserialize_json(
                data["Predicate"]
            )
        )
    return out
