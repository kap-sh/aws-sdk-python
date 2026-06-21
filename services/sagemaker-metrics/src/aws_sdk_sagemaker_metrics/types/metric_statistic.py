"""Generated from Smithy shape ``com.amazonaws.sagemakermetrics#MetricStatistic``."""

from typing import Literal, TypeAlias, cast

MetricStatistic: TypeAlias = Literal[
    "Min",
    "Max",
    "Avg",
    "Count",
    "StdDev",
    "Last",
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricStatistic) -> str:
    return value


def deserialize_json(data: str) -> MetricStatistic:
    return cast(MetricStatistic, data)
