"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerGatewayMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

PlayerGatewayMode: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
    "REQUIRED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
        "REQUIRED",
    )
)


def serialize_aws_json_1_1(value: PlayerGatewayMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PlayerGatewayMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PlayerGatewayMode value: {data!r}")
    return cast(PlayerGatewayMode, data)
