"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerProtectionPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

GameServerProtectionPolicy: TypeAlias = Literal[
    "NO_PROTECTION",
    "FULL_PROTECTION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_PROTECTION",
        "FULL_PROTECTION",
    )
)


def serialize_aws_json_1_1(value: GameServerProtectionPolicy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GameServerProtectionPolicy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GameServerProtectionPolicy value: {data!r}"
        )
    return cast(GameServerProtectionPolicy, data)
