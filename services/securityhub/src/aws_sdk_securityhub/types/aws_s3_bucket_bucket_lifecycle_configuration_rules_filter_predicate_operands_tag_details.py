"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetails(
    TypedDict, closed=True
):
    key: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The tag key.</p>"""
    value: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The tag value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetails,
) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(
    data: dict,
) -> AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetails:
    out: AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetails = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
