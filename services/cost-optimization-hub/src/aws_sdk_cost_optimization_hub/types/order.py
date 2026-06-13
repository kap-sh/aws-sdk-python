"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#Order``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_optimization_hub.errors import DeserializationError

Order: TypeAlias = Literal[
    "Asc",
    "Desc",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Asc",
        "Desc",
    )
)


def serialize_aws_json_1_0(value: Order) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Order:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Order value: {data!r}")
    return cast(Order, data)
