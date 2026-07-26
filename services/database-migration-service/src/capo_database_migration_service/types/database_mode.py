"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DatabaseMode``."""

from typing import Literal, TypeAlias, cast

DatabaseMode: TypeAlias = Literal[
    "default",
    "babelfish",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DatabaseMode:
    return cast(DatabaseMode, data)
