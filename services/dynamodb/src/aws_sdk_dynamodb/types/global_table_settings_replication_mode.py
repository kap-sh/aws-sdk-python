"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalTableSettingsReplicationMode``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_dynamodb.errors import DeserializationError

GlobalTableSettingsReplicationMode: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "ENABLED_WITH_OVERRIDES",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
        "ENABLED_WITH_OVERRIDES",
    )
)


def serialize_aws_json_1_0(value: GlobalTableSettingsReplicationMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> GlobalTableSettingsReplicationMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GlobalTableSettingsReplicationMode value: {data!r}"
        )
    return cast(GlobalTableSettingsReplicationMode, data)
