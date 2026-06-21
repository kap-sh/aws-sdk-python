"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#PostgreSQLAuthenticationMethod``."""

from typing import Literal, TypeAlias, cast

PostgreSQLAuthenticationMethod: TypeAlias = Literal[
    "password",
    "iam",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PostgreSQLAuthenticationMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PostgreSQLAuthenticationMethod:
    return cast(PostgreSQLAuthenticationMethod, data)
