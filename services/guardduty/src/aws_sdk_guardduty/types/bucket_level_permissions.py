"""Generated from Smithy shape ``com.amazonaws.guardduty#BucketLevelPermissions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.access_control_list
    import aws_sdk_guardduty.types.block_public_access
    import aws_sdk_guardduty.types.bucket_policy


class BucketLevelPermissions(TypedDict):
    access_control_list: NotRequired[
        "aws_sdk_guardduty.types.access_control_list.AccessControlList"
    ]
    """<p>Contains information on how Access Control Policies are applied to the bucket.</p>"""
    bucket_policy: NotRequired["aws_sdk_guardduty.types.bucket_policy.BucketPolicy"]
    """<p>Contains information on the bucket policies for the S3 bucket.</p>"""
    block_public_access: NotRequired[
        "aws_sdk_guardduty.types.block_public_access.BlockPublicAccess"
    ]
    """<p>Contains information on which account level S3 Block Public Access settings are applied to the S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BucketLevelPermissions) -> dict:
    out: dict = {}
    if "access_control_list" in value:
        import aws_sdk_guardduty.types.access_control_list

        out["accessControlList"] = (
            aws_sdk_guardduty.types.access_control_list.serialize_json(
                value["access_control_list"]
            )
        )
    if "bucket_policy" in value:
        import aws_sdk_guardduty.types.bucket_policy

        out["bucketPolicy"] = aws_sdk_guardduty.types.bucket_policy.serialize_json(
            value["bucket_policy"]
        )
    if "block_public_access" in value:
        import aws_sdk_guardduty.types.block_public_access

        out["blockPublicAccess"] = (
            aws_sdk_guardduty.types.block_public_access.serialize_json(
                value["block_public_access"]
            )
        )
    return out


def deserialize_json(data: dict) -> BucketLevelPermissions:
    out: BucketLevelPermissions = {}  # type: ignore[typeddict-item]
    if "accessControlList" in data:
        import aws_sdk_guardduty.types.access_control_list

        out["access_control_list"] = (
            aws_sdk_guardduty.types.access_control_list.deserialize_json(
                data["accessControlList"]
            )
        )
    if "bucketPolicy" in data:
        import aws_sdk_guardduty.types.bucket_policy

        out["bucket_policy"] = aws_sdk_guardduty.types.bucket_policy.deserialize_json(
            data["bucketPolicy"]
        )
    if "blockPublicAccess" in data:
        import aws_sdk_guardduty.types.block_public_access

        out["block_public_access"] = (
            aws_sdk_guardduty.types.block_public_access.deserialize_json(
                data["blockPublicAccess"]
            )
        )
    return out
