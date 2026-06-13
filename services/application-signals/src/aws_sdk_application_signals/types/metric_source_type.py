"""Generated from Smithy shape ``com.amazonaws.applicationsignals#MetricSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_signals.errors import DeserializationError

MetricSourceType: TypeAlias = Literal[
    "ServiceOperation",
    "CloudWatchMetric",
    "ServiceDependency",
    "AppMonitor",
    "Canary",
    "Service",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ServiceOperation",
        "CloudWatchMetric",
        "ServiceDependency",
        "AppMonitor",
        "Canary",
        "Service",
    )
)


def serialize_json(value: MetricSourceType) -> str:
    return value


def deserialize_json(data: str) -> MetricSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MetricSourceType value: {data!r}")
    return cast(MetricSourceType, data)
