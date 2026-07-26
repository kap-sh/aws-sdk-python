"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer


class AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetails(
    TypedDict, closed=True
):
    days_after_initiation: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The number of days after which Amazon S3 cancels an incomplete multipart upload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetails,
) -> dict:
    out: dict = {}
    if "days_after_initiation" in value:
        out["DaysAfterInitiation"] = value["days_after_initiation"]
    return out


def deserialize_json(
    data: dict,
) -> AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetails:
    out: AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetails = {}  # type: ignore[typeddict-item]
    if "DaysAfterInitiation" in data:
        out["days_after_initiation"] = data["DaysAfterInitiation"]
    return out
