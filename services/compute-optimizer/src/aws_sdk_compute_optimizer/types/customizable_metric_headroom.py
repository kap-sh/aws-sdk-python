"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#CustomizableMetricHeadroom``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

CustomizableMetricHeadroom: TypeAlias = Literal[
    "PERCENT_30",
    "PERCENT_20",
    "PERCENT_10",
    "PERCENT_0",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PERCENT_30",
        "PERCENT_20",
        "PERCENT_10",
        "PERCENT_0",
    )
)


def serialize_aws_json_1_0(value: CustomizableMetricHeadroom) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CustomizableMetricHeadroom:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CustomizableMetricHeadroom value: {data!r}"
        )
    return cast(CustomizableMetricHeadroom, data)
