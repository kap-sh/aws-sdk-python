"""Generated from Smithy shape ``com.amazonaws.networkmanager#RoutingPolicyDirection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

RoutingPolicyDirection: TypeAlias = Literal[
    "inbound",
    "outbound",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "inbound",
        "outbound",
    )
)


def serialize_json(value: RoutingPolicyDirection) -> str:
    return value


def deserialize_json(data: str) -> RoutingPolicyDirection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RoutingPolicyDirection value: {data!r}")
    return cast(RoutingPolicyDirection, data)
