"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerGroupDeleteOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

GameServerGroupDeleteOption: TypeAlias = Literal[
    "SAFE_DELETE",
    "FORCE_DELETE",
    "RETAIN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SAFE_DELETE",
        "FORCE_DELETE",
        "RETAIN",
    )
)


def serialize_aws_json_1_1(value: GameServerGroupDeleteOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GameServerGroupDeleteOption:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GameServerGroupDeleteOption value: {data!r}"
        )
    return cast(GameServerGroupDeleteOption, data)
