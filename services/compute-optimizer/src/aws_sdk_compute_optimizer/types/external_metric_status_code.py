"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExternalMetricStatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

ExternalMetricStatusCode: TypeAlias = Literal[
    "NO_EXTERNAL_METRIC_SET",
    "INTEGRATION_SUCCESS",
    "DATADOG_INTEGRATION_ERROR",
    "DYNATRACE_INTEGRATION_ERROR",
    "NEWRELIC_INTEGRATION_ERROR",
    "INSTANA_INTEGRATION_ERROR",
    "INSUFFICIENT_DATADOG_METRICS",
    "INSUFFICIENT_DYNATRACE_METRICS",
    "INSUFFICIENT_NEWRELIC_METRICS",
    "INSUFFICIENT_INSTANA_METRICS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_EXTERNAL_METRIC_SET",
        "INTEGRATION_SUCCESS",
        "DATADOG_INTEGRATION_ERROR",
        "DYNATRACE_INTEGRATION_ERROR",
        "NEWRELIC_INTEGRATION_ERROR",
        "INSTANA_INTEGRATION_ERROR",
        "INSUFFICIENT_DATADOG_METRICS",
        "INSUFFICIENT_DYNATRACE_METRICS",
        "INSUFFICIENT_NEWRELIC_METRICS",
        "INSUFFICIENT_INSTANA_METRICS",
    )
)


def serialize_aws_json_1_0(value: ExternalMetricStatusCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExternalMetricStatusCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExternalMetricStatusCode value: {data!r}")
    return cast(ExternalMetricStatusCode, data)
