"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerIpProtocolSupported``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

GameServerIpProtocolSupported: TypeAlias = Literal[
    "IPv4",
    "DUAL_STACK",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IPv4",
        "DUAL_STACK",
    )
)


def serialize_aws_json_1_1(value: GameServerIpProtocolSupported) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GameServerIpProtocolSupported:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GameServerIpProtocolSupported value: {data!r}"
        )
    return cast(GameServerIpProtocolSupported, data)
