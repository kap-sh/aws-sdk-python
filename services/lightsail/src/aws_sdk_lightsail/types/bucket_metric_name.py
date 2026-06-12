"""Generated from Smithy shape ``com.amazonaws.lightsail#BucketMetricName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

BucketMetricName: TypeAlias = Literal[
    "BucketSizeBytes",
    "NumberOfObjects",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BucketSizeBytes",
        "NumberOfObjects",
    )
)


def serialize_aws_json_1_1(value: BucketMetricName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BucketMetricName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BucketMetricName value: {data!r}")
    return cast(BucketMetricName, data)
