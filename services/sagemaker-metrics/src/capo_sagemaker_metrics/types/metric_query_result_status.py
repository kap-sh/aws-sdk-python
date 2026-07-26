"""Generated from Smithy shape ``com.amazonaws.sagemakermetrics#MetricQueryResultStatus``."""

from typing import Literal, TypeAlias, cast

MetricQueryResultStatus: TypeAlias = Literal[
    "Complete",
    "Truncated",
    "InternalError",
    "ValidationError",
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricQueryResultStatus) -> str:
    return value


def deserialize_json(data: str) -> MetricQueryResultStatus:
    return cast(MetricQueryResultStatus, data)
