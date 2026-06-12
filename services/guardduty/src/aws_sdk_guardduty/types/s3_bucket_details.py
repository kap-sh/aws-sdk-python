"""Generated from Smithy shape ``com.amazonaws.guardduty#S3BucketDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.s3_bucket_detail

S3BucketDetails: TypeAlias = list[
    "aws_sdk_guardduty.types.s3_bucket_detail.S3BucketDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: S3BucketDetails) -> list:
    import aws_sdk_guardduty.types.s3_bucket_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_guardduty.types.s3_bucket_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> S3BucketDetails:
    import aws_sdk_guardduty.types.s3_bucket_detail

    out: S3BucketDetails = []
    for item in data:
        out.append(aws_sdk_guardduty.types.s3_bucket_detail.deserialize_json(item))
    return out
