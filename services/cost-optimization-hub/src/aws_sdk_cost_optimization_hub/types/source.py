"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#Source``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_optimization_hub.errors import DeserializationError

Source: TypeAlias = Literal[
    "ComputeOptimizer",
    "CostExplorer",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ComputeOptimizer",
        "CostExplorer",
    )
)


def serialize_aws_json_1_0(value: Source) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Source:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Source value: {data!r}")
    return cast(Source, data)
