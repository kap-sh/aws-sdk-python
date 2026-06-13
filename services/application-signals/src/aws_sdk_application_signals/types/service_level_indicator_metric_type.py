"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceLevelIndicatorMetricType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_signals.errors import DeserializationError

ServiceLevelIndicatorMetricType: TypeAlias = Literal[
    "LATENCY",
    "AVAILABILITY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LATENCY",
        "AVAILABILITY",
    )
)


def serialize_json(value: ServiceLevelIndicatorMetricType) -> str:
    return value


def deserialize_json(data: str) -> ServiceLevelIndicatorMetricType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ServiceLevelIndicatorMetricType value: {data!r}"
        )
    return cast(ServiceLevelIndicatorMetricType, data)
