"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerHealthCheck``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

GameServerHealthCheck: TypeAlias = Literal["HEALTHY",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("HEALTHY",))


def serialize_aws_json_1_1(value: GameServerHealthCheck) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GameServerHealthCheck:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GameServerHealthCheck value: {data!r}")
    return cast(GameServerHealthCheck, data)
