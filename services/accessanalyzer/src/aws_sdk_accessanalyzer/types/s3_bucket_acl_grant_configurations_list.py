"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#S3BucketAclGrantConfigurationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.s3_bucket_acl_grant_configuration

S3BucketAclGrantConfigurationsList: TypeAlias = list[
    "aws_sdk_accessanalyzer.types.s3_bucket_acl_grant_configuration.S3BucketAclGrantConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: S3BucketAclGrantConfigurationsList) -> list:
    import aws_sdk_accessanalyzer.types.s3_bucket_acl_grant_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_accessanalyzer.types.s3_bucket_acl_grant_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> S3BucketAclGrantConfigurationsList:
    import aws_sdk_accessanalyzer.types.s3_bucket_acl_grant_configuration

    out: S3BucketAclGrantConfigurationsList = []
    for item in data:
        out.append(
            aws_sdk_accessanalyzer.types.s3_bucket_acl_grant_configuration.deserialize_json(
                item
            )
        )
    return out
