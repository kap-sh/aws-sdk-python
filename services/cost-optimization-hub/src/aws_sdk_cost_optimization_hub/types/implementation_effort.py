"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ImplementationEffort``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_optimization_hub.errors import DeserializationError

ImplementationEffort: TypeAlias = Literal[
    "VeryLow",
    "Low",
    "Medium",
    "High",
    "VeryHigh",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VeryLow",
        "Low",
        "Medium",
        "High",
        "VeryHigh",
    )
)


def serialize_aws_json_1_0(value: ImplementationEffort) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ImplementationEffort:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImplementationEffort value: {data!r}")
    return cast(ImplementationEffort, data)
