"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerGatewayStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

PlayerGatewayStatus: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_aws_json_1_1(value: PlayerGatewayStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PlayerGatewayStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PlayerGatewayStatus value: {data!r}")
    return cast(PlayerGatewayStatus, data)
