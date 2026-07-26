"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketObjectLockConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_s3_bucket_object_lock_configuration_rule_details
    import capo_securityhub.types.non_empty_string


class AwsS3BucketObjectLockConfiguration(TypedDict, closed=True):
    object_lock_enabled: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> Indicates whether the bucket has an Object Lock configuration enabled. </p>"""
    rule: NotRequired[
        "capo_securityhub.types.aws_s3_bucket_object_lock_configuration_rule_details.AwsS3BucketObjectLockConfigurationRuleDetails"
    ]
    """<p> Specifies the Object Lock rule for the specified object. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketObjectLockConfiguration) -> dict:
    out: dict = {}
    if "object_lock_enabled" in value:
        out["ObjectLockEnabled"] = value["object_lock_enabled"]
    if "rule" in value:
        import capo_securityhub.types.aws_s3_bucket_object_lock_configuration_rule_details

        out["Rule"] = (
            capo_securityhub.types.aws_s3_bucket_object_lock_configuration_rule_details.serialize_json(
                value["rule"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsS3BucketObjectLockConfiguration:
    out: AwsS3BucketObjectLockConfiguration = {}  # type: ignore[typeddict-item]
    if "ObjectLockEnabled" in data:
        out["object_lock_enabled"] = data["ObjectLockEnabled"]
    if "Rule" in data:
        import capo_securityhub.types.aws_s3_bucket_object_lock_configuration_rule_details

        out["rule"] = (
            capo_securityhub.types.aws_s3_bucket_object_lock_configuration_rule_details.deserialize_json(
                data["Rule"]
            )
        )
    return out
