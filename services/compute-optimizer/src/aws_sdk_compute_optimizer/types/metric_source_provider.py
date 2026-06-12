"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#MetricSourceProvider``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

MetricSourceProvider: TypeAlias = Literal["CloudWatchApplicationInsights",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("CloudWatchApplicationInsights",))


def serialize_aws_json_1_0(value: MetricSourceProvider) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MetricSourceProvider:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MetricSourceProvider value: {data!r}")
    return cast(MetricSourceProvider, data)
