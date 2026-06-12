"""Generated from Smithy shape ``com.amazonaws.sagemakermetrics#MetricStatistic``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker_metrics.errors import DeserializationError

MetricStatistic: TypeAlias = Literal[
    "Min",
    "Max",
    "Avg",
    "Count",
    "StdDev",
    "Last",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Min",
        "Max",
        "Avg",
        "Count",
        "StdDev",
        "Last",
    )
)


def serialize_json(value: MetricStatistic) -> str:
    return value


def deserialize_json(data: str) -> MetricStatistic:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MetricStatistic value: {data!r}")
    return cast(MetricStatistic, data)
