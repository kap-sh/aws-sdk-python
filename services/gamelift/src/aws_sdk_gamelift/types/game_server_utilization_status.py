"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerUtilizationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

GameServerUtilizationStatus: TypeAlias = Literal[
    "AVAILABLE",
    "UTILIZED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "UTILIZED",
    )
)


def serialize_aws_json_1_1(value: GameServerUtilizationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GameServerUtilizationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GameServerUtilizationStatus value: {data!r}"
        )
    return cast(GameServerUtilizationStatus, data)
