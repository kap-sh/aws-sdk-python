"""Generated from Smithy shape ``com.amazonaws.odb#DatabaseType``."""

from typing import Literal, TypeAlias, cast

DatabaseType: TypeAlias = Literal[
    "REGULAR",
    "CLONE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DatabaseType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DatabaseType:
    return cast(DatabaseType, data)
