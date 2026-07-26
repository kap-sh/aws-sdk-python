"""Generated from Smithy shape ``com.amazonaws.shield#LogBucketList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_shield.types.log_bucket

LogBucketList: TypeAlias = list["capo_shield.types.log_bucket.LogBucket"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogBucketList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> LogBucketList:
    return list(data)
