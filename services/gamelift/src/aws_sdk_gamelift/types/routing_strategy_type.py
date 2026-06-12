"""Generated from Smithy shape ``com.amazonaws.gamelift#RoutingStrategyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

RoutingStrategyType: TypeAlias = Literal[
    "SIMPLE",
    "TERMINAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SIMPLE",
        "TERMINAL",
    )
)


def serialize_aws_json_1_1(value: RoutingStrategyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RoutingStrategyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RoutingStrategyType value: {data!r}")
    return cast(RoutingStrategyType, data)
