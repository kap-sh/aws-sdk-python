"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerGroupAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

GameServerGroupAction: TypeAlias = Literal["REPLACE_INSTANCE_TYPES",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("REPLACE_INSTANCE_TYPES",))


def serialize_aws_json_1_1(value: GameServerGroupAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GameServerGroupAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GameServerGroupAction value: {data!r}")
    return cast(GameServerGroupAction, data)
