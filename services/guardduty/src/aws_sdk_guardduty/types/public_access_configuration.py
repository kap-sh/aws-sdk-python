"""Generated from Smithy shape ``com.amazonaws.guardduty#PublicAccessConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.public_access_status
    import aws_sdk_guardduty.types.public_acl_ignore_behavior
    import aws_sdk_guardduty.types.public_bucket_restrict_behavior


class PublicAccessConfiguration(TypedDict):
    public_acl_access: NotRequired[
        "aws_sdk_guardduty.types.public_access_status.PublicAccessStatus"
    ]
    """<p>Indicates whether or not there is a setting that allows public access to the Amazon S3 buckets through access control lists (ACLs).</p>"""
    public_policy_access: NotRequired[
        "aws_sdk_guardduty.types.public_access_status.PublicAccessStatus"
    ]
    """<p>Indicates whether or not there is a setting that allows public access to the Amazon S3 bucket policy.</p>"""
    public_acl_ignore_behavior: NotRequired[
        "aws_sdk_guardduty.types.public_acl_ignore_behavior.PublicAclIgnoreBehavior"
    ]
    """<p>Indicates whether or not there is a setting that ignores all public access control lists (ACLs) on the Amazon S3 bucket and the objects that it contains.</p>"""
    public_bucket_restrict_behavior: NotRequired[
        "aws_sdk_guardduty.types.public_bucket_restrict_behavior.PublicBucketRestrictBehavior"
    ]
    """<p>Indicates whether or not there is a setting that restricts access to the bucket with specified policies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublicAccessConfiguration) -> dict:
    out: dict = {}
    if "public_acl_access" in value:
        import aws_sdk_guardduty.types.public_access_status

        out["publicAclAccess"] = (
            aws_sdk_guardduty.types.public_access_status.serialize_json(
                value["public_acl_access"]
            )
        )
    if "public_policy_access" in value:
        import aws_sdk_guardduty.types.public_access_status

        out["publicPolicyAccess"] = (
            aws_sdk_guardduty.types.public_access_status.serialize_json(
                value["public_policy_access"]
            )
        )
    if "public_acl_ignore_behavior" in value:
        import aws_sdk_guardduty.types.public_acl_ignore_behavior

        out["publicAclIgnoreBehavior"] = (
            aws_sdk_guardduty.types.public_acl_ignore_behavior.serialize_json(
                value["public_acl_ignore_behavior"]
            )
        )
    if "public_bucket_restrict_behavior" in value:
        import aws_sdk_guardduty.types.public_bucket_restrict_behavior

        out["publicBucketRestrictBehavior"] = (
            aws_sdk_guardduty.types.public_bucket_restrict_behavior.serialize_json(
                value["public_bucket_restrict_behavior"]
            )
        )
    return out


def deserialize_json(data: dict) -> PublicAccessConfiguration:
    out: PublicAccessConfiguration = {}  # type: ignore[typeddict-item]
    if "publicAclAccess" in data:
        import aws_sdk_guardduty.types.public_access_status

        out["public_acl_access"] = (
            aws_sdk_guardduty.types.public_access_status.deserialize_json(
                data["publicAclAccess"]
            )
        )
    if "publicPolicyAccess" in data:
        import aws_sdk_guardduty.types.public_access_status

        out["public_policy_access"] = (
            aws_sdk_guardduty.types.public_access_status.deserialize_json(
                data["publicPolicyAccess"]
            )
        )
    if "publicAclIgnoreBehavior" in data:
        import aws_sdk_guardduty.types.public_acl_ignore_behavior

        out["public_acl_ignore_behavior"] = (
            aws_sdk_guardduty.types.public_acl_ignore_behavior.deserialize_json(
                data["publicAclIgnoreBehavior"]
            )
        )
    if "publicBucketRestrictBehavior" in data:
        import aws_sdk_guardduty.types.public_bucket_restrict_behavior

        out["public_bucket_restrict_behavior"] = (
            aws_sdk_guardduty.types.public_bucket_restrict_behavior.deserialize_json(
                data["publicBucketRestrictBehavior"]
            )
        )
    return out
