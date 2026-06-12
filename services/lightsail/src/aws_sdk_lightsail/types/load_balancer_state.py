"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

LoadBalancerState: TypeAlias = Literal[
    "active",
    "provisioning",
    "active_impaired",
    "failed",
    "unknown",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "active",
        "provisioning",
        "active_impaired",
        "failed",
        "unknown",
    )
)


def serialize_aws_json_1_1(value: LoadBalancerState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LoadBalancerState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LoadBalancerState value: {data!r}")
    return cast(LoadBalancerState, data)
