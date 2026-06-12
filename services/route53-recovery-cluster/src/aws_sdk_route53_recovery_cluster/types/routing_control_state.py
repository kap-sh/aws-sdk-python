"""Generated from Smithy shape ``com.amazonaws.route53recoverycluster#RoutingControlState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53_recovery_cluster.errors import DeserializationError

RoutingControlState: TypeAlias = Literal[
    "On",
    "Off",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "On",
        "Off",
    )
)


def serialize_aws_json_1_0(value: RoutingControlState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RoutingControlState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RoutingControlState value: {data!r}")
    return cast(RoutingControlState, data)
