"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketObjectLockConfigurationRuleDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_s3_bucket_object_lock_configuration_rule_default_retention_details


class AwsS3BucketObjectLockConfigurationRuleDetails(TypedDict, closed=True):
    default_retention: NotRequired[
        "capo_securityhub.types.aws_s3_bucket_object_lock_configuration_rule_default_retention_details.AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetails"
    ]
    """<p> The default Object Lock retention mode and period that you want to apply to new objects placed in the specified bucket. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketObjectLockConfigurationRuleDetails) -> dict:
    out: dict = {}
    if "default_retention" in value:
        import capo_securityhub.types.aws_s3_bucket_object_lock_configuration_rule_default_retention_details

        out["DefaultRetention"] = (
            capo_securityhub.types.aws_s3_bucket_object_lock_configuration_rule_default_retention_details.serialize_json(
                value["default_retention"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsS3BucketObjectLockConfigurationRuleDetails:
    out: AwsS3BucketObjectLockConfigurationRuleDetails = {}  # type: ignore[typeddict-item]
    if "DefaultRetention" in data:
        import capo_securityhub.types.aws_s3_bucket_object_lock_configuration_rule_default_retention_details

        out["default_retention"] = (
            capo_securityhub.types.aws_s3_bucket_object_lock_configuration_rule_default_retention_details.deserialize_json(
                data["DefaultRetention"]
            )
        )
    return out
