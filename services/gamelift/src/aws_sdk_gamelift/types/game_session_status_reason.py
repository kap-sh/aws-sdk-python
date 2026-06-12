"""Generated from Smithy shape ``com.amazonaws.gamelift#GameSessionStatusReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

GameSessionStatusReason: TypeAlias = Literal[
    "INTERRUPTED",
    "TRIGGERED_ON_PROCESS_TERMINATE",
    "FORCE_TERMINATED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTERRUPTED",
        "TRIGGERED_ON_PROCESS_TERMINATE",
        "FORCE_TERMINATED",
    )
)


def serialize_aws_json_1_1(value: GameSessionStatusReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GameSessionStatusReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GameSessionStatusReason value: {data!r}")
    return cast(GameSessionStatusReason, data)
