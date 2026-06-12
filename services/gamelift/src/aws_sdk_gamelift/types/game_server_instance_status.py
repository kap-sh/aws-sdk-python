"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerInstanceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

GameServerInstanceStatus: TypeAlias = Literal[
    "ACTIVE",
    "DRAINING",
    "SPOT_TERMINATING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DRAINING",
        "SPOT_TERMINATING",
    )
)


def serialize_aws_json_1_1(value: GameServerInstanceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GameServerInstanceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GameServerInstanceStatus value: {data!r}")
    return cast(GameServerInstanceStatus, data)
