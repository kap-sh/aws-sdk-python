"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#SqlServerAuthenticationMethod``."""

from typing import Literal, TypeAlias, cast

SqlServerAuthenticationMethod: TypeAlias = Literal[
    "password",
    "kerberos",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SqlServerAuthenticationMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SqlServerAuthenticationMethod:
    return cast(SqlServerAuthenticationMethod, data)
