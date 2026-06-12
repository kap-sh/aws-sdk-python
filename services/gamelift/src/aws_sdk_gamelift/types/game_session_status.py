"""Generated from Smithy shape ``com.amazonaws.gamelift#GameSessionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

GameSessionStatus: TypeAlias = Literal[
    "ACTIVE",
    "ACTIVATING",
    "TERMINATED",
    "TERMINATING",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "ACTIVATING",
        "TERMINATED",
        "TERMINATING",
        "ERROR",
    )
)


def serialize_aws_json_1_1(value: GameSessionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GameSessionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GameSessionStatus value: {data!r}")
    return cast(GameSessionStatus, data)
