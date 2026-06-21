"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#MigrationTypeValue``."""

from typing import Literal, TypeAlias, cast

MigrationTypeValue: TypeAlias = Literal[
    "full-load",
    "cdc",
    "full-load-and-cdc",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MigrationTypeValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MigrationTypeValue:
    return cast(MigrationTypeValue, data)
