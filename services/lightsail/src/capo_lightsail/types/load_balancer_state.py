"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerState``."""

from typing import Literal, TypeAlias, cast

LoadBalancerState: TypeAlias = Literal[
    "active",
    "provisioning",
    "active_impaired",
    "failed",
    "unknown",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoadBalancerState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LoadBalancerState:
    return cast(LoadBalancerState, data)
