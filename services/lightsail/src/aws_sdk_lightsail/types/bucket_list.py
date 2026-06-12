"""Generated from Smithy shape ``com.amazonaws.lightsail#BucketList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.bucket

BucketList: TypeAlias = list["aws_sdk_lightsail.types.bucket.Bucket"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BucketList) -> list:
    import aws_sdk_lightsail.types.bucket

    out: list = []
    for item in value:
        out.append(aws_sdk_lightsail.types.bucket.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BucketList:
    import aws_sdk_lightsail.types.bucket

    out: BucketList = []
    for item in data:
        out.append(aws_sdk_lightsail.types.bucket.deserialize_aws_json_1_1(item))
    return out
