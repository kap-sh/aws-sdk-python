"""Generated from Smithy shape ``com.amazonaws.gamelift#PlacementFallbackStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

PlacementFallbackStrategy: TypeAlias = Literal[
    "DEFAULT_AFTER_SINGLE_PASS",
    "NONE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT_AFTER_SINGLE_PASS",
        "NONE",
    )
)


def serialize_aws_json_1_1(value: PlacementFallbackStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PlacementFallbackStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PlacementFallbackStrategy value: {data!r}")
    return cast(PlacementFallbackStrategy, data)
