"""Generated from Smithy shape ``com.amazonaws.gamelift#GameSessionPlacementState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

GameSessionPlacementState: TypeAlias = Literal[
    "PENDING",
    "FULFILLED",
    "CANCELLED",
    "TIMED_OUT",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "FULFILLED",
        "CANCELLED",
        "TIMED_OUT",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: GameSessionPlacementState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GameSessionPlacementState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GameSessionPlacementState value: {data!r}")
    return cast(GameSessionPlacementState, data)
