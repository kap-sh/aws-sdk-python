"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetails(TypedDict):
    days: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p> The number of days that you want to specify for the default retention period. </p>"""
    mode: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The default Object Lock retention mode you want to apply to new objects placed in the specified bucket. </p>"""
    years: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p> The number of years that you want to specify for the default retention period. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetails,
) -> dict:
    out: dict = {}
    if "days" in value:
        out["Days"] = value["days"]
    if "mode" in value:
        out["Mode"] = value["mode"]
    if "years" in value:
        out["Years"] = value["years"]
    return out


def deserialize_json(
    data: dict,
) -> AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetails:
    out: AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetails = {}  # type: ignore[typeddict-item]
    if "Days" in data:
        out["days"] = data["Days"]
    if "Mode" in data:
        out["mode"] = data["Mode"]
    if "Years" in data:
        out["years"] = data["Years"]
    return out
