"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#CustomizableMetricThreshold``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

CustomizableMetricThreshold: TypeAlias = Literal[
    "P90",
    "P95",
    "P99_5",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "P90",
        "P95",
        "P99_5",
    )
)


def serialize_aws_json_1_0(value: CustomizableMetricThreshold) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CustomizableMetricThreshold:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CustomizableMetricThreshold value: {data!r}"
        )
    return cast(CustomizableMetricThreshold, data)
