"""Generated from Smithy shape ``com.amazonaws.gamelift#BalancingStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

BalancingStrategy: TypeAlias = Literal[
    "SPOT_ONLY",
    "SPOT_PREFERRED",
    "ON_DEMAND_ONLY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SPOT_ONLY",
        "SPOT_PREFERRED",
        "ON_DEMAND_ONLY",
    )
)


def serialize_aws_json_1_1(value: BalancingStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BalancingStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BalancingStrategy value: {data!r}")
    return cast(BalancingStrategy, data)
