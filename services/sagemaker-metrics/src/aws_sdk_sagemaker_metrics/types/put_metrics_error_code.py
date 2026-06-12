"""Generated from Smithy shape ``com.amazonaws.sagemakermetrics#PutMetricsErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker_metrics.errors import DeserializationError

PutMetricsErrorCode: TypeAlias = Literal[
    "METRIC_LIMIT_EXCEEDED",
    "INTERNAL_ERROR",
    "VALIDATION_ERROR",
    "CONFLICT_ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "METRIC_LIMIT_EXCEEDED",
        "INTERNAL_ERROR",
        "VALIDATION_ERROR",
        "CONFLICT_ERROR",
    )
)


def serialize_json(value: PutMetricsErrorCode) -> str:
    return value


def deserialize_json(data: str) -> PutMetricsErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PutMetricsErrorCode value: {data!r}")
    return cast(PutMetricsErrorCode, data)
