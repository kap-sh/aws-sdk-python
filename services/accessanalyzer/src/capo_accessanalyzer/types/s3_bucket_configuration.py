"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#S3BucketConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.s3_access_point_configurations_map
    import capo_accessanalyzer.types.s3_bucket_acl_grant_configurations_list
    import capo_accessanalyzer.types.s3_bucket_policy
    import capo_accessanalyzer.types.s3_public_access_block_configuration


class S3BucketConfiguration(TypedDict, closed=True):
    bucket_policy: NotRequired[
        "capo_accessanalyzer.types.s3_bucket_policy.S3BucketPolicy"
    ]
    """<p>The proposed bucket policy for the Amazon S3 bucket.</p>"""
    bucket_acl_grants: NotRequired[
        "capo_accessanalyzer.types.s3_bucket_acl_grant_configurations_list.S3BucketAclGrantConfigurationsList"
    ]
    """<p>The proposed list of ACL grants for the Amazon S3 bucket. You can propose up to 100 ACL grants per bucket. If the proposed grant configuration is for an existing bucket, the access preview uses the proposed list of grant configurations in place of the existing grants. Otherwise, the access preview uses the existing grants for the bucket.</p>"""
    bucket_public_access_block: NotRequired[
        "capo_accessanalyzer.types.s3_public_access_block_configuration.S3PublicAccessBlockConfiguration"
    ]
    """<p>The proposed block public access configuration for the Amazon S3 bucket.</p>"""
    access_points: NotRequired[
        "capo_accessanalyzer.types.s3_access_point_configurations_map.S3AccessPointConfigurationsMap"
    ]
    """<p>The configuration of Amazon S3 access points or multi-region access points for the bucket. You can propose up to 10 new access points per bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3BucketConfiguration) -> dict:
    out: dict = {}
    if "bucket_policy" in value:
        out["bucketPolicy"] = value["bucket_policy"]
    if "bucket_acl_grants" in value:
        import capo_accessanalyzer.types.s3_bucket_acl_grant_configurations_list

        out["bucketAclGrants"] = (
            capo_accessanalyzer.types.s3_bucket_acl_grant_configurations_list.serialize_json(
                value["bucket_acl_grants"]
            )
        )
    if "bucket_public_access_block" in value:
        import capo_accessanalyzer.types.s3_public_access_block_configuration

        out["bucketPublicAccessBlock"] = (
            capo_accessanalyzer.types.s3_public_access_block_configuration.serialize_json(
                value["bucket_public_access_block"]
            )
        )
    if "access_points" in value:
        import capo_accessanalyzer.types.s3_access_point_configurations_map

        out["accessPoints"] = (
            capo_accessanalyzer.types.s3_access_point_configurations_map.serialize_json(
                value["access_points"]
            )
        )
    return out


def deserialize_json(data: dict) -> S3BucketConfiguration:
    out: S3BucketConfiguration = {}  # type: ignore[typeddict-item]
    if "bucketPolicy" in data:
        out["bucket_policy"] = data["bucketPolicy"]
    if "bucketAclGrants" in data:
        import capo_accessanalyzer.types.s3_bucket_acl_grant_configurations_list

        out["bucket_acl_grants"] = (
            capo_accessanalyzer.types.s3_bucket_acl_grant_configurations_list.deserialize_json(
                data["bucketAclGrants"]
            )
        )
    if "bucketPublicAccessBlock" in data:
        import capo_accessanalyzer.types.s3_public_access_block_configuration

        out["bucket_public_access_block"] = (
            capo_accessanalyzer.types.s3_public_access_block_configuration.deserialize_json(
                data["bucketPublicAccessBlock"]
            )
        )
    if "accessPoints" in data:
        import capo_accessanalyzer.types.s3_access_point_configurations_map

        out["access_points"] = (
            capo_accessanalyzer.types.s3_access_point_configurations_map.deserialize_json(
                data["accessPoints"]
            )
        )
    return out
