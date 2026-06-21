"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalTableSettingsReplicationMode``."""

from typing import Literal, TypeAlias, cast

GlobalTableSettingsReplicationMode: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "ENABLED_WITH_OVERRIDES",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GlobalTableSettingsReplicationMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> GlobalTableSettingsReplicationMode:
    return cast(GlobalTableSettingsReplicationMode, data)
