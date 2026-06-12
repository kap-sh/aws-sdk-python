"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerSessionCreationPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

PlayerSessionCreationPolicy: TypeAlias = Literal[
    "ACCEPT_ALL",
    "DENY_ALL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCEPT_ALL",
        "DENY_ALL",
    )
)


def serialize_aws_json_1_1(value: PlayerSessionCreationPolicy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PlayerSessionCreationPolicy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PlayerSessionCreationPolicy value: {data!r}"
        )
    return cast(PlayerSessionCreationPolicy, data)
