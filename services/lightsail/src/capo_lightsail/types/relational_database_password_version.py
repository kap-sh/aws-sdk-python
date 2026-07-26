"""Generated from Smithy shape ``com.amazonaws.lightsail#RelationalDatabasePasswordVersion``."""

from typing import Literal, TypeAlias, cast

RelationalDatabasePasswordVersion: TypeAlias = Literal[
    "CURRENT",
    "PREVIOUS",
    "PENDING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelationalDatabasePasswordVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RelationalDatabasePasswordVersion:
    return cast(RelationalDatabasePasswordVersion, data)
