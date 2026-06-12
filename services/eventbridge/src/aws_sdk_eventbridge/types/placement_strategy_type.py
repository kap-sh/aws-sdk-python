"""Generated from Smithy shape ``com.amazonaws.eventbridge#PlacementStrategyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eventbridge.errors import DeserializationError

PlacementStrategyType: TypeAlias = Literal[
    "random",
    "spread",
    "binpack",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "random",
        "spread",
        "binpack",
    )
)


def serialize_aws_json_1_1(value: PlacementStrategyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PlacementStrategyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PlacementStrategyType value: {data!r}")
    return cast(PlacementStrategyType, data)
