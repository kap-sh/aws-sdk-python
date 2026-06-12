"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#BucketList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudsearch_domain.types.bucket

BucketList: TypeAlias = list["aws_sdk_cloudsearch_domain.types.bucket.Bucket"]


# --- restJson1 ser/de ---
def serialize_json(value: BucketList) -> list:
    import aws_sdk_cloudsearch_domain.types.bucket

    out: list = []
    for item in value:
        out.append(aws_sdk_cloudsearch_domain.types.bucket.serialize_json(item))
    return out


def deserialize_json(data: list) -> BucketList:
    import aws_sdk_cloudsearch_domain.types.bucket

    out: BucketList = []
    for item in data:
        out.append(aws_sdk_cloudsearch_domain.types.bucket.deserialize_json(item))
    return out
