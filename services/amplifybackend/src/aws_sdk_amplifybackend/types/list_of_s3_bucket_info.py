"""Generated from Smithy shape ``com.amazonaws.amplifybackend#ListOfS3BucketInfo``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.s3_bucket_info

ListOfS3BucketInfo: TypeAlias = list[
    "aws_sdk_amplifybackend.types.s3_bucket_info.S3BucketInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfS3BucketInfo) -> list:
    import aws_sdk_amplifybackend.types.s3_bucket_info

    out: list = []
    for item in value:
        out.append(aws_sdk_amplifybackend.types.s3_bucket_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfS3BucketInfo:
    import aws_sdk_amplifybackend.types.s3_bucket_info

    out: ListOfS3BucketInfo = []
    for item in data:
        out.append(aws_sdk_amplifybackend.types.s3_bucket_info.deserialize_json(item))
    return out
