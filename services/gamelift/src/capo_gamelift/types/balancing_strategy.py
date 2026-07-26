"""Generated from Smithy shape ``com.amazonaws.gamelift#BalancingStrategy``."""

from typing import Literal, TypeAlias, cast

BalancingStrategy: TypeAlias = Literal[
    "SPOT_ONLY",
    "SPOT_PREFERRED",
    "ON_DEMAND_ONLY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BalancingStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BalancingStrategy:
    return cast(BalancingStrategy, data)
