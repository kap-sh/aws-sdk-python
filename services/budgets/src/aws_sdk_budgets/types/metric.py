"""Generated from Smithy shape ``com.amazonaws.budgets#Metric``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_budgets.errors import DeserializationError

Metric: TypeAlias = Literal[
    "BlendedCost",
    "UnblendedCost",
    "AmortizedCost",
    "NetUnblendedCost",
    "NetAmortizedCost",
    "UsageQuantity",
    "NormalizedUsageAmount",
    "Hours",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BlendedCost",
        "UnblendedCost",
        "AmortizedCost",
        "NetUnblendedCost",
        "NetAmortizedCost",
        "UsageQuantity",
        "NormalizedUsageAmount",
        "Hours",
    )
)


def serialize_aws_json_1_1(value: Metric) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Metric:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Metric value: {data!r}")
    return cast(Metric, data)
