"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DmsSslModeValue``."""

from typing import Literal, TypeAlias, cast

DmsSslModeValue: TypeAlias = Literal[
    "none",
    "require",
    "verify-ca",
    "verify-full",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DmsSslModeValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DmsSslModeValue:
    return cast(DmsSslModeValue, data)
