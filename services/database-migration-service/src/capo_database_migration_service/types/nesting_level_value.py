"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#NestingLevelValue``."""

from typing import Literal, TypeAlias, cast

NestingLevelValue: TypeAlias = Literal[
    "none",
    "one",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NestingLevelValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NestingLevelValue:
    return cast(NestingLevelValue, data)
