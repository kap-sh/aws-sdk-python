"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketObjectLockConfigurationRuleDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_s3_bucket_object_lock_configuration_rule_default_retention_details


class AwsS3BucketObjectLockConfigurationRuleDetails(TypedDict, closed=True):
    default_retention: NotRequired[
        "aws_sdk_securityhub.types.aws_s3_bucket_object_lock_configuration_rule_default_retention_details.AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetails"
    ]
    """<p> The default Object Lock retention mode and period that you want to apply to new objects placed in the specified bucket. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketObjectLockConfigurationRuleDetails) -> dict:
    out: dict = {}
    if "default_retention" in value:
        import aws_sdk_securityhub.types.aws_s3_bucket_object_lock_configuration_rule_default_retention_details

        out["DefaultRetention"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_object_lock_configuration_rule_default_retention_details.serialize_json(
                value["default_retention"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsS3BucketObjectLockConfigurationRuleDetails:
    out: AwsS3BucketObjectLockConfigurationRuleDetails = {}  # type: ignore[typeddict-item]
    if "DefaultRetention" in data:
        import aws_sdk_securityhub.types.aws_s3_bucket_object_lock_configuration_rule_default_retention_details

        out["default_retention"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_object_lock_configuration_rule_default_retention_details.deserialize_json(
                data["DefaultRetention"]
            )
        )
    return out
