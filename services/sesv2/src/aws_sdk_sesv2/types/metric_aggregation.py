"""Generated from Smithy shape ``com.amazonaws.sesv2#MetricAggregation``."""

from typing import Literal, TypeAlias, cast

"""<p>The aggregation to apply to a metric, can be one of the following:</p> <ul> <li> <p> <code>VOLUME</code> - The volume of events for this metric.</p> </li> <li> <p> <code>RATE</code> - The rate for this metric relative to the <code>SEND</code> metric volume.</p> </li> </ul>"""
MetricAggregation: TypeAlias = Literal[
    "RATE",
    "VOLUME",
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricAggregation) -> str:
    return value


def deserialize_json(data: str) -> MetricAggregation:
    return cast(MetricAggregation, data)
