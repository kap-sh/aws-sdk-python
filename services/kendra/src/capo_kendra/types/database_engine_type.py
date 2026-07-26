"""Generated from Smithy shape ``com.amazonaws.kendra#DatabaseEngineType``."""

from typing import Literal, TypeAlias, cast

DatabaseEngineType: TypeAlias = Literal[
    "RDS_AURORA_MYSQL",
    "RDS_AURORA_POSTGRESQL",
    "RDS_MYSQL",
    "RDS_POSTGRESQL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseEngineType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DatabaseEngineType:
    return cast(DatabaseEngineType, data)
