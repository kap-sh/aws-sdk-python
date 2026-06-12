"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerGroupStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

GameServerGroupStatus: TypeAlias = Literal[
    "NEW",
    "ACTIVATING",
    "ACTIVE",
    "DELETE_SCHEDULED",
    "DELETING",
    "DELETED",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NEW",
        "ACTIVATING",
        "ACTIVE",
        "DELETE_SCHEDULED",
        "DELETING",
        "DELETED",
        "ERROR",
    )
)


def serialize_aws_json_1_1(value: GameServerGroupStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GameServerGroupStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GameServerGroupStatus value: {data!r}")
    return cast(GameServerGroupStatus, data)
