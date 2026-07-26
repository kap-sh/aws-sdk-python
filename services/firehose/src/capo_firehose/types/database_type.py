"""Generated from Smithy shape ``com.amazonaws.firehose#DatabaseType``."""

from typing import Literal, TypeAlias, cast

DatabaseType: TypeAlias = Literal[
    "MySQL",
    "PostgreSQL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DatabaseType:
    return cast(DatabaseType, data)
