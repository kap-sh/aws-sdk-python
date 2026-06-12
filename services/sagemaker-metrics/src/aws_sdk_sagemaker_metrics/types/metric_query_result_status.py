"""Generated from Smithy shape ``com.amazonaws.sagemakermetrics#MetricQueryResultStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker_metrics.errors import DeserializationError

MetricQueryResultStatus: TypeAlias = Literal[
    "Complete",
    "Truncated",
    "InternalError",
    "ValidationError",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Complete",
        "Truncated",
        "InternalError",
        "ValidationError",
    )
)


def serialize_json(value: MetricQueryResultStatus) -> str:
    return value


def deserialize_json(data: str) -> MetricQueryResultStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MetricQueryResultStatus value: {data!r}")
    return cast(MetricQueryResultStatus, data)
