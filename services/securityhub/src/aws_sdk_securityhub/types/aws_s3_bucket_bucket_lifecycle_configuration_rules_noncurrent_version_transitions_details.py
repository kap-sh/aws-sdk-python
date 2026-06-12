"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails(
    TypedDict
):
    days: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of days that an object is noncurrent before Amazon S3 can perform the associated action.</p>"""
    storage_class: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The class of storage to change the object to after the object is noncurrent for the specified number of days.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails,
) -> dict:
    out: dict = {}
    if "days" in value:
        out["Days"] = value["days"]
    if "storage_class" in value:
        out["StorageClass"] = value["storage_class"]
    return out


def deserialize_json(
    data: dict,
) -> AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails:
    out: AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails = {}  # type: ignore[typeddict-item]
    if "Days" in data:
        out["days"] = data["Days"]
    if "StorageClass" in data:
        out["storage_class"] = data["StorageClass"]
    return out
