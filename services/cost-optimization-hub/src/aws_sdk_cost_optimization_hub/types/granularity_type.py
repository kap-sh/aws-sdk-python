"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#GranularityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_optimization_hub.errors import DeserializationError

"""<p>The time granularity for aggregating the cost efficiency metrics.</p>"""
GranularityType: TypeAlias = Literal[
    "Daily",
    "Monthly",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Daily",
        "Monthly",
    )
)


def serialize_aws_json_1_0(value: GranularityType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> GranularityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GranularityType value: {data!r}")
    return cast(GranularityType, data)
