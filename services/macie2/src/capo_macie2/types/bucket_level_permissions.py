"""Generated from Smithy shape ``com.amazonaws.macie2#BucketLevelPermissions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.access_control_list
    import capo_macie2.types.block_public_access
    import capo_macie2.types.bucket_policy


class BucketLevelPermissions(TypedDict, closed=True):
    access_control_list: NotRequired[
        "capo_macie2.types.access_control_list.AccessControlList"
    ]
    """<p>The permissions settings of the access control list (ACL) for the bucket. This value is null if an ACL hasn't been defined for the bucket.</p>"""
    block_public_access: NotRequired[
        "capo_macie2.types.block_public_access.BlockPublicAccess"
    ]
    """<p>The block public access settings for the bucket.</p>"""
    bucket_policy: NotRequired["capo_macie2.types.bucket_policy.BucketPolicy"]
    """<p>The permissions settings of the bucket policy for the bucket. This value is null if a bucket policy hasn't been defined for the bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BucketLevelPermissions) -> dict:
    out: dict = {}
    if "access_control_list" in value:
        import capo_macie2.types.access_control_list

        out["accessControlList"] = capo_macie2.types.access_control_list.serialize_json(
            value["access_control_list"]
        )
    if "block_public_access" in value:
        import capo_macie2.types.block_public_access

        out["blockPublicAccess"] = capo_macie2.types.block_public_access.serialize_json(
            value["block_public_access"]
        )
    if "bucket_policy" in value:
        import capo_macie2.types.bucket_policy

        out["bucketPolicy"] = capo_macie2.types.bucket_policy.serialize_json(
            value["bucket_policy"]
        )
    return out


def deserialize_json(data: dict) -> BucketLevelPermissions:
    out: BucketLevelPermissions = {}  # type: ignore[typeddict-item]
    if "accessControlList" in data:
        import capo_macie2.types.access_control_list

        out["access_control_list"] = (
            capo_macie2.types.access_control_list.deserialize_json(
                data["accessControlList"]
            )
        )
    if "blockPublicAccess" in data:
        import capo_macie2.types.block_public_access

        out["block_public_access"] = (
            capo_macie2.types.block_public_access.deserialize_json(
                data["blockPublicAccess"]
            )
        )
    if "bucketPolicy" in data:
        import capo_macie2.types.bucket_policy

        out["bucket_policy"] = capo_macie2.types.bucket_policy.deserialize_json(
            data["bucketPolicy"]
        )
    return out
