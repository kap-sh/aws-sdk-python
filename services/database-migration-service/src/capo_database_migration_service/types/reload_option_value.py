"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReloadOptionValue``."""

from typing import Literal, TypeAlias, cast

ReloadOptionValue: TypeAlias = Literal[
    "data-reload",
    "validate-only",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReloadOptionValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReloadOptionValue:
    return cast(ReloadOptionValue, data)
