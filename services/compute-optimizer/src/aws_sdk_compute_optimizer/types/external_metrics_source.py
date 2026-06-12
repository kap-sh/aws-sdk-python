"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExternalMetricsSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

ExternalMetricsSource: TypeAlias = Literal[
    "Datadog",
    "Dynatrace",
    "NewRelic",
    "Instana",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Datadog",
        "Dynatrace",
        "NewRelic",
        "Instana",
    )
)


def serialize_aws_json_1_0(value: ExternalMetricsSource) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExternalMetricsSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExternalMetricsSource value: {data!r}")
    return cast(ExternalMetricsSource, data)
