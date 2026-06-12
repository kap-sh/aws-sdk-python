"""Generated from Smithy shape ``com.amazonaws.lightsail#DistributionMetricName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

DistributionMetricName: TypeAlias = Literal[
    "Requests",
    "BytesDownloaded",
    "BytesUploaded",
    "TotalErrorRate",
    "Http4xxErrorRate",
    "Http5xxErrorRate",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Requests",
        "BytesDownloaded",
        "BytesUploaded",
        "TotalErrorRate",
        "Http4xxErrorRate",
        "Http5xxErrorRate",
    )
)


def serialize_aws_json_1_1(value: DistributionMetricName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DistributionMetricName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DistributionMetricName value: {data!r}")
    return cast(DistributionMetricName, data)
