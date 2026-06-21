"""Generated from Smithy shape ``com.amazonaws.lightsail#BucketMetricName``."""

from typing import Literal, TypeAlias, cast

BucketMetricName: TypeAlias = Literal[
    "BucketSizeBytes",
    "NumberOfObjects",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BucketMetricName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BucketMetricName:
    return cast(BucketMetricName, data)
