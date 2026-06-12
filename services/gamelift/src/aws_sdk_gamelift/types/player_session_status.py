"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerSessionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

PlayerSessionStatus: TypeAlias = Literal[
    "RESERVED",
    "ACTIVE",
    "COMPLETED",
    "TIMEDOUT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RESERVED",
        "ACTIVE",
        "COMPLETED",
        "TIMEDOUT",
    )
)


def serialize_aws_json_1_1(value: PlayerSessionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PlayerSessionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PlayerSessionStatus value: {data!r}")
    return cast(PlayerSessionStatus, data)
