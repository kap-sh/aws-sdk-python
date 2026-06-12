"""Generated from Smithy shape ``com.amazonaws.ssmguiconnect#S3Buckets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_guiconnect.types.s3_bucket

S3Buckets: TypeAlias = list["aws_sdk_ssm_guiconnect.types.s3_bucket.S3Bucket"]


# --- restJson1 ser/de ---
def serialize_json(value: S3Buckets) -> list:
    import aws_sdk_ssm_guiconnect.types.s3_bucket

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm_guiconnect.types.s3_bucket.serialize_json(item))
    return out


def deserialize_json(data: list) -> S3Buckets:
    import aws_sdk_ssm_guiconnect.types.s3_bucket

    out: S3Buckets = []
    for item in data:
        out.append(aws_sdk_ssm_guiconnect.types.s3_bucket.deserialize_json(item))
    return out
