"""Generated from Smithy shape ``com.amazonaws.servicediscovery#RoutingPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_servicediscovery.errors import DeserializationError

RoutingPolicy: TypeAlias = Literal[
    "MULTIVALUE",
    "WEIGHTED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MULTIVALUE",
        "WEIGHTED",
    )
)


def serialize_aws_json_1_1(value: RoutingPolicy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RoutingPolicy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RoutingPolicy value: {data!r}")
    return cast(RoutingPolicy, data)
