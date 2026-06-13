"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#SummaryMetrics``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_optimization_hub.errors import DeserializationError

SummaryMetrics: TypeAlias = Literal["SavingsPercentage",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("SavingsPercentage",))


def serialize_aws_json_1_0(value: SummaryMetrics) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SummaryMetrics:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SummaryMetrics value: {data!r}")
    return cast(SummaryMetrics, data)
