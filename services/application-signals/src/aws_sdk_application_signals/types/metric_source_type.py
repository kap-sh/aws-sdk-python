"""Generated from Smithy shape ``com.amazonaws.applicationsignals#MetricSourceType``."""

from typing import Literal, TypeAlias, cast

MetricSourceType: TypeAlias = Literal[
    "ServiceOperation",
    "CloudWatchMetric",
    "ServiceDependency",
    "AppMonitor",
    "Canary",
    "Service",
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricSourceType) -> str:
    return value


def deserialize_json(data: str) -> MetricSourceType:
    return cast(MetricSourceType, data)
