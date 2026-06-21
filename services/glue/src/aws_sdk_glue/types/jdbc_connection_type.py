"""Generated from Smithy shape ``com.amazonaws.glue#JDBCConnectionType``."""

from typing import Literal, TypeAlias, cast

JDBCConnectionType: TypeAlias = Literal[
    "sqlserver",
    "mysql",
    "oracle",
    "postgresql",
    "redshift",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JDBCConnectionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JDBCConnectionType:
    return cast(JDBCConnectionType, data)
