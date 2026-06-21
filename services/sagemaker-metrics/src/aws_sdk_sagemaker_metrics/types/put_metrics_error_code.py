"""Generated from Smithy shape ``com.amazonaws.sagemakermetrics#PutMetricsErrorCode``."""

from typing import Literal, TypeAlias, cast

PutMetricsErrorCode: TypeAlias = Literal[
    "METRIC_LIMIT_EXCEEDED",
    "INTERNAL_ERROR",
    "VALIDATION_ERROR",
    "CONFLICT_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: PutMetricsErrorCode) -> str:
    return value


def deserialize_json(data: str) -> PutMetricsErrorCode:
    return cast(PutMetricsErrorCode, data)
