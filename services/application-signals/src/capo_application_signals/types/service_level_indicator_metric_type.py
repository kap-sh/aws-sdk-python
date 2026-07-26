"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceLevelIndicatorMetricType``."""

from typing import Literal, TypeAlias, cast

ServiceLevelIndicatorMetricType: TypeAlias = Literal[
    "LATENCY",
    "AVAILABILITY",
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceLevelIndicatorMetricType) -> str:
    return value


def deserialize_json(data: str) -> ServiceLevelIndicatorMetricType:
    return cast(ServiceLevelIndicatorMetricType, data)
