"""Generated from Smithy shape ``com.amazonaws.sagemaker#MetricPublishFrequencyInSeconds``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

MetricPublishFrequencyInSeconds: TypeAlias = Literal[
    10,
    30,
    60,
    120,
    180,
    240,
    300,
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[int] = frozenset(
    (
        10,
        30,
        60,
        120,
        180,
        240,
        300,
    )
)


def serialize_aws_json_1_1(value: MetricPublishFrequencyInSeconds) -> int:
    return value


def deserialize_aws_json_1_1(data: int) -> MetricPublishFrequencyInSeconds:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MetricPublishFrequencyInSeconds value: {data!r}"
        )
    return cast(MetricPublishFrequencyInSeconds, data)
